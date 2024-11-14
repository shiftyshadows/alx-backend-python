#!/usr/bin/env python3
"""
   This module defines the asychronous
   coroutine: measure_runtime.
"""
import importlib
import asyncio
import time

# Import async_comprehension from the previous task using importlib
async_comprehension_module = importlib.import_module('1-async_comprehension')
async_comprehension = async_comprehension_module.async_comprehension


async def measure_runtime():
    """
    Coroutine that measures the time taken to execute async_comprehension
    four times in parallel and returns the total runtime.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_runtime = time.time() - start_time
    return total_runtime
