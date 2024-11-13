#!/usr/bin/env python3
"""
   This module defines the function make_multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
                                  the result of multiplying it by `multiplier`.
    """
    def multiplier_func(value: float) -> float:
        return value * multiplier

    return multiplier_func
