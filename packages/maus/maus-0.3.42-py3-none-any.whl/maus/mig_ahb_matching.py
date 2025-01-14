"""
MAUS is the MIG AHB Utility stack.
This module contains methods to merge data from Message Implementation Guide and Anwendungshandbuch
"""
from itertools import groupby
from typing import List, Optional, Sequence, Set, Tuple

from more_itertools import first, first_true, last

from maus.models.anwendungshandbuch import _VERSION, AhbLine, DeepAnwendungshandbuch, FlatAnwendungshandbuch
from maus.models.edifact_components import (
    DataElement,
    DataElementFreeText,
    DataElementValuePool,
    EdifactStack,
    Segment,
    SegmentGroup,
    ValuePoolEntry,
    derive_data_type_from_segment_code,
)
from maus.models.message_implementation_guide import SegmentGroupHierarchy
from maus.navigation import AhbLocation, calculate_distance, determine_locations
from maus.reader.mig_reader import MigReader


def merge_lines_with_same_data_element(
    ahb_lines: Sequence[AhbLine], first_stack: Optional[EdifactStack]
) -> DataElement:
    """
    Merges lines that have the same data element into a single data element instance which is returned
    """
    distinct_data_element_keys = {ahb_line.data_element for ahb_line in ahb_lines}
    if len(distinct_data_element_keys) != 1:
        raise ValueError(
            "You must only use this function with lines that share the same data element but the "
            f"parameter ahb_lines contains: {', '.join([x or '' for x in distinct_data_element_keys])} "
        )
    result: DataElement
    discriminator = None
    if first_stack is not None:
        discriminator = first_stack.to_json_path()
    if ahb_lines[0].value_pool_entry is not None:
        result = DataElementValuePool(
            discriminator=discriminator,
            value_pool=[],
            data_element_id=ahb_lines[0].data_element,  # type:ignore[arg-type]
            entered_input=None,
        )
        for data_element_value_entry in ahb_lines:
            if not data_element_value_entry.ahb_expression:
                # value pool entries with empty/None AHB expression shall not be included
                # https://github.com/Hochfrequenz/mig_ahb_utility_stack/issues/38
                continue
            value_pool_entry = ValuePoolEntry(
                qualifier=data_element_value_entry.value_pool_entry,  # type:ignore[arg-type]
                meaning=data_element_value_entry.name.strip(),  # type:ignore[assignment,union-attr]
                ahb_expression=data_element_value_entry.ahb_expression,
            )
            result.value_pool.append(value_pool_entry)  # type:ignore[index]
    else:
        result = DataElementFreeText(
            entered_input=None,
            ahb_expression=ahb_lines[0].ahb_expression,  # type:ignore[arg-type]
            discriminator=discriminator,
            data_element_id=first(  # type:ignore[union-attr]
                ahb_lines, lambda line: line.data_element is not None
            ).data_element,  # type:ignore[arg-type]
        )
        # a free text field never spans more than 1 line

        data_type = derive_data_type_from_segment_code(ahb_lines[0].segment_code)  # type:ignore[arg-type]
        if data_type is not None:
            result.value_type = data_type
    return result


def _remove_qualifier(location: AhbLocation) -> AhbLocation:
    """
    returns a copy of location but with an empty qualifier
    """
    result: AhbLocation = AhbLocation(
        qualifier=None,
        layers=location.layers,
        data_element_id=location.data_element_id,
        segment_code=location.segment_code,
    )
    return result


# I'm aware the function is too long; Let's first make it work, then split up into separate functions.
# pylint:disable=too-many-locals, too-many-branches, too-many-statements
# https://github.com/Hochfrequenz/mig_ahb_utility_stack/issues/205
def to_deep_ahb(
    flat_ahb: FlatAnwendungshandbuch, segment_group_hierarchy: SegmentGroupHierarchy, mig_reader: MigReader
) -> DeepAnwendungshandbuch:
    """
    Converts a flat ahb into a nested ahb using the provided segment hierarchy
    """
    result = DeepAnwendungshandbuch(meta=flat_ahb.meta, lines=[])
    result.meta.maus_version = _VERSION
    parent_group_lists: List[List[SegmentGroup]] = []
    used_stacks: Set[str] = set()
    # The following lists are _not_ a view into the lines that are going to follow (hence no name starting with "next")
    # Instead the lists are a reference to the respective attribute _inside_ the upper hierarchy element.
    # So whenever we e.g. run into a data element, we can "remember" to where the data element shall be appended.
    # The lists are our "reference" so that each element deeper into the hierarchy (e.g. data elements) knows to which
    # parent (e.g. segment) it belongs.
    # Note that the lists are never assigned to anything.
    # + they're always instantiated empty
    # + then we store a reference to the list in `append_next_foo_here`
    # + when ever we find a foo downstream we append it to this list (and thereby assign it to its parent)
    # + when ever we find a new parent element, this variable that holds the reference to the old (now previous) parent
    # is replaced with a reference to the new parent to all the downstream elements to come.
    append_next_segments_here: List[Segment]  #: is instantiated/replaced whenever a new segment group is created
    append_next_sg_here: List[SegmentGroup]  #: is instantiated/replaced whenever a new segment group is created
    append_next_data_elements_here: List[DataElement]  #: is instantiated/replaced whenever a new segment is created
    previous_position: AhbLocation
    for position, layer_group in groupby(
        determine_locations(segment_group_hierarchy, flat_ahb.lines),
        key=lambda line_and_position: _remove_qualifier(line_and_position[1]),
    ):
        layer_group: List[Tuple[AhbLine, AhbLocation]] = list(layer_group)  # type:ignore[no-redef]
        data_element_lines = [x[0] for x in layer_group]  # index 1 is the position
        if not any((True for line in data_element_lines if line.segment_code is not None)):
            continue  # section heading only
        stack: EdifactStack
        try:
            if len(data_element_lines) == 1:
                position = layer_group[0][1]  # type:ignore[index]
            stack = mig_reader.get_edifact_stack(position)
        except ValueError:
            # if the AHB/MIG matching does not work as expected, set your breakpoints here
            stack = None  # type:ignore[assignment]
            if len(data_element_lines) > 1:
                for _position in (x[1] for x in layer_group):
                    try:
                        stack = mig_reader.get_edifact_stack(layer_group[0][1])  # type:ignore[index]
                        break
                    except ValueError:
                        pass
        if any((True for line in data_element_lines if line.data_element is not None)):
            if not any((True for line in data_element_lines if line.ahb_expression is not None)):
                # if none of the items is marked with an ahb expression it's probably not required in this AHB
                continue
            data_element = merge_lines_with_same_data_element(data_element_lines, first_stack=stack)
            try:
                append_next_data_elements_here.append(data_element)  # pylint:disable=used-before-assignment
            except UnboundLocalError as unbound_local_error:
                raise ValueError(f"No segment has been created for {stack}") from unbound_local_error
        else:
            first_line = first(data_element_lines)
            last_line = last(data_element_lines)
            if (
                first_line.segment_group_key == last(position.layers).segment_group_key
                and last(position.layers).opening_segment_code == last_line.segment_code
                and stack is not None
                and stack.to_json_path() not in used_stacks
                and first_line.ahb_expression is not None
            ):
                # a new segment group has been opened
                segment_group = SegmentGroup(
                    discriminator=stack.to_json_path(),
                    # type:ignore[arg-type] # might be None now, will be replaced later
                    ahb_expression=first_line.ahb_expression.strip(),
                    segments=[],
                    segment_groups=[],
                    ahb_line_index=first_line.index,
                )
                used_stacks.add(stack.to_json_path())
                append_next_segments_here = segment_group.segments  # type:ignore[assignment]
                if segment_group.discriminator == '$["Dokument"][0]["Nachricht"][0]':
                    result.lines.append(segment_group)
                    append_next_sg_here = segment_group.segment_groups  # type:ignore[assignment]
                    parent_group_lists.append(result.lines)
                elif position.is_sub_location_of(previous_position):  # pylint:disable=used-before-assignment
                    append_next_sg_here.append(segment_group)
                    parent_group_lists.append(append_next_sg_here)
                    append_next_sg_here = segment_group.segment_groups  # type:ignore[assignment]
                else:
                    distance = calculate_distance(previous_position, position)
                    for _ in range(0, distance.layers_up):
                        try:
                            append_next_sg_here = parent_group_lists.pop()
                        except IndexError as index_error:
                            raise ValueError(f"Couldn't move from {previous_position} to {position}") from index_error
                    for _ in range(0, distance.layers_down - 1):
                        parent_group_lists.append(append_next_sg_here)
                        append_next_sg_here = last(append_next_sg_here).segment_groups  # type:ignore[assignment]
                    append_next_sg_here.append(segment_group)
                    parent_group_lists.append(append_next_sg_here)
                    append_next_sg_here = segment_group.segment_groups  # type:ignore[assignment]

            assert last_line.data_element is None
            assert last_line.segment_code is not None
            # these assertion are because we assume that the lines always come like this:
            # Section Heading
            # SGx Foo      <-- a line with only the segment code but no actual content; this is where we're right now
            first_expression_line: Optional[AhbLine] = first_true(
                data_element_lines, default=None, pred=lambda l: l is not None and l.ahb_expression
            )
            if first_expression_line is None:
                continue
            first_expression: str = first_expression_line.ahb_expression  # type:ignore[assignment]
            discriminator: str
            if stack is None:
                # this is a pretty ugly hack. when we cannot find a position in the MIG, then we just stringify the
                # position and by doing so hope, that the reader of the maus can use it somehow
                discriminator = str(position)
            else:
                # this should be the default path
                discriminator = stack.to_json_path()
            segment = Segment(
                discriminator=discriminator,  # todo: sometimes the discriminator is not as sharp as it could have been
                data_elements=[],
                ahb_expression=first_expression,
                section_name=first_line.section_name,
                ahb_line_index=first_line.index,
            )
            append_next_data_elements_here = segment.data_elements
            append_next_segments_here.append(segment)
        previous_position = position
    return result
