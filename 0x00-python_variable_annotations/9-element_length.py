#!/usr/bin/env python3
"""
   This module defines the function element_length.
"""
from typing import List, Tuple, Sequence


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing elements and their lengths.

    Args:
        lst (List[Sequence]): A list of sequences (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
                                    an element from `lst` and its length.
    """
    return [(i, len(i)) for i in lst]
