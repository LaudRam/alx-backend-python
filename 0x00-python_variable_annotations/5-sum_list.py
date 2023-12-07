#!/usr/bin/env python3
""" Function returns the sum of floating numbers in a list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Accepts a list of floating numbers and return the sum """
    return float(sum(input_list))
