#!/usr/bin/env python3
"""
    This module defines the async
    coroutine: async_generator.
"""
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields a random number between 0 and 10,
    with a 1-second delay in each of its 10 iterations.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
