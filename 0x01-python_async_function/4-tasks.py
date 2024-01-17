#!/usr/bin/env python3
""" contains a coroutine that runs concurrently with wait_random"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """a coroutine that runs with wait_random"""

    result = await asyncio.gather(*(
             task_wait_random(max_delay) for i in range(n)))
    return sorted(result)
