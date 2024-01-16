#!/usr/bin/env python3
""" contains my first coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits a certain time between 0 and max delay
       before returning"""

    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
