#!/usr/bin/env python3
"""contains element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """finds the length of 1st just annotating"""

    return [(i, len(i)) for i in lst]
