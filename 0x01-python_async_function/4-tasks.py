#!/usr/bin/env python3
""" This module defines the function: task_wait_n. """
import asyncio
import importlib
from typing import List

task_wait_random = importlib.import_module("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates n asyncio tasks that run with a delay up to max_delay,
    then collects and returns the results in ascending order.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: List of delay times in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
