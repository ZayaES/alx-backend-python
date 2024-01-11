#!/usr/bin/env python3
"""contains to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns tuple of key and value times 2"""

    return (k, float(v**2))
