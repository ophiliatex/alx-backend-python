#!/usr/bin/env python3
"""The module contains a function that
returns the length of an element."""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the length of an element."""
    return [(i, len(i)) for i in lst]
