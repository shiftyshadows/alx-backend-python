#!/usr/bin/env python3
"""
   This module defines the function sum_mixed_list.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of all numbers in mxd_lst as a float.
    """
    return sum(mxd_lst)
