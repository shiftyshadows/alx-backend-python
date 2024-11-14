#!/usr/bin/env python3
""" This module defines an asynchronous coroutine"""
import asyncio
import importlib.util
from typing import List

# Dynamically import wait_random from 0-basic_async_syntax.py
spec = importlib.util.spec_from_file_location(
    "wait_random", "./0-basic_async_syntax.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns
    a list of the delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []

    # Gather all tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    # As tasks complete, append their results to the list
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

