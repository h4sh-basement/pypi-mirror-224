"""
This module contains (static) functions that process single lxml.etree Elements.
Each function is separately unit tested.
"""
import re
from typing import List, Literal, Optional

# pylint:disable=no-name-in-module
from lxml.etree import Element  # type:ignore[import]


def get_segment_group_key_or_none(element: Element) -> Optional[str]:
    """
    returns the segment group of element if present; None otherwise
    """
    if "ref" in element.attrib and element.attrib["ref"].startswith("SG"):
        # the trivial case
        return element.attrib["ref"]
    return None


#: a regex to match a ref-segment: https://regex101.com/r/D81bbO/1
_single_nested_qualifier_pattern = re.compile(
    r"^(?P<segment_code>[A-Z]+):\d+:(?:\d+|\(\d+,\d+\))\[(?:\w+:)+\w+:?=(?P<qualifier>[A-Z\d]+)\]$"
)

#: a regex to match multiple ref/key segments: https://regex101.com/r/6XooRL/2
_multiple_nestes_qualifiers_pattern = re.compile(
    r"(?P<segment_code>[A-Z]+):\d+:(?:\d+|\(\d+,\d+\))\[(?P<inner>(?:(?:[A-Z]+:)?\d+:\d+=[A-Z\d]+\|?)+)\]$"
)


def get_nested_qualifiers(attrib_key: Literal["ref", "key"], element: Element) -> Optional[List[str]]:
    """
    returns the nested qualifier of an element if present; None otherwise
    we still return None instead of an empty list, because all the framework around this method actually check for None
    instead of empty lists
    """
    if attrib_key in element.attrib:
        body: str = element.attrib[attrib_key]
        single_match = _single_nested_qualifier_pattern.match(body)
        if single_match:
            return [single_match["qualifier"]]
        multi_match = _multiple_nestes_qualifiers_pattern.match(body)
        if multi_match:
            # if body == "QTY:1:1[1:0=265|1:0=Z10|1:0=Z08]"
            # then multi_match["inner"] is "1:0=265|1:0=Z10|1:0=Z08"
            return [expression.split("=")[1] for expression in multi_match["inner"].split("|")]
    return None


def get_ahb_name_or_none(element: Element) -> Optional[str]:
    """
    returns the ahbName of element if present; None otherwise
    """
    if "ahbName" in element.attrib:
        return element.attrib["ahbName"]
    return None
