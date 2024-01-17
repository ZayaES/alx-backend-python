#!/usr/bin/env python3
""" contains a coroutine that runs concurrently with wait_random"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """a coroutine that runs with wait_random"""

    result = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(result)
