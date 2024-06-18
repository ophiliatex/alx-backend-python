#!/usr/bin/env python3
"""Converts an integer to a key-value pair"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts an integer to a key-value pair"""

    return tuple((k, v ** 2))
