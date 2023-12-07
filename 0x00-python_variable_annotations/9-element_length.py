#!/usr/bin/env python3
""" Module for element length """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Iterate through sequence """
    return [(i, len(i)) for i in lst]
