#!/usr/bin/env python3
""" Function returns a function that multiplies a float by a multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Accepts a floating number as parameter """
    def myFunction(multiply: float) -> float:
        """ Creating the multiply """
        return float(multiply * multiplier)
    return myFunction
