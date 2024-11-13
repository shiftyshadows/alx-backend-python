#!/usr/bin/env python3
"""
   This module defines the function element_length.
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing elements and their lengths.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
                                    an element from `lst` and its length.
    """
    return [(i, len(i)) for i in lst]
