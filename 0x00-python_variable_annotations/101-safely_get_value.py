#!/usr/bin/env python3
""" This module defines the function: safely_get_value."""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """Return the value from the dictionary for the given key, or a default
    if the key is not present.

    Args:
        dct (Mapping): A dictionary-like mapping.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The default value to return if key
                                            is not in dct.

    Returns:
        Union[Any, T]: The value associated with the key, or the default if
                       the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
