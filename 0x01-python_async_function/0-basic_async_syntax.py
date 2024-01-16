#!/usr/bin/env python3
""" contains my first coroutine """


import asyncio, random

async def wait_random(max_delay = 10):
    """waits a certain time between 0 and max delay
       before returning"""

    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
