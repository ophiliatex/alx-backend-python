#!/usr/bin/env python3
"""The sum of all numbers in the list."""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Return the sum of all numbers in the list."""

    return sum(mxd_list)
