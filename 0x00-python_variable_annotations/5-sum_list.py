#!/usr/bin/env python3
"""
   This module defines the function sum_list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of all floats in input_list.
    """
    return sum(input_list)
