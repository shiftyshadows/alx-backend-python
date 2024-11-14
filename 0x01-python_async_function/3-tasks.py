#!/usr/bin/env python3
""" This module defines the function: task_wait_random. """
import asyncio
import importlib

# Dynamically import wait_random from 0-basic_async_syntax
wait_random = importlib.import_module("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: A task that runs the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
