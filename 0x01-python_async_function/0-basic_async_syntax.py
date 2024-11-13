#!/usr/bin/env python3
""" This module defines an asynchronous coroutine. """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns it.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
