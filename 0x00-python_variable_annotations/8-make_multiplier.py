#!/usr/bin/env python3
"""contains make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """makes a float a multiplier and returns a number times multiplier"""

    return lambda number: number * multiplier
