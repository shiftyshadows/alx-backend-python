#!/usr/bin/env python3
"""
   This module defines the function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of an int/float as a float.

    Args:
        k (str): A string.
        v (Union[int, float]): An integer or float value.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`
                           and the second element is the square of `v` as a float.
    """
    return (k, float(v ** 2))
