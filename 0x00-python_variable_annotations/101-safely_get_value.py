#!/usr/bin/env python3
"""The module contains the safely_get_value function."""
from typing import TypeVar, Mapping, Union, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Returns a safe value of a dictionary."""
    if key in dct:
        return dct[key]
    else:
        return default
