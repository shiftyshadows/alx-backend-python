#!/usr/bin/env python3
""" This module defines the function: zoom_array. """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list with each element in lst repeated factor times.

    Args:
        lst (Tuple): A tuple of elements.
        factor (int): The repeat factor for each element in the tuple.

    Returns:
        List: A list where each element is repeated factor times.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Converted to a tuple to match function annotation

zoom_2x = zoom_array(array)  # Default factor of 2
zoom_3x = zoom_array(array, 3)  # Pass an integer for factor
