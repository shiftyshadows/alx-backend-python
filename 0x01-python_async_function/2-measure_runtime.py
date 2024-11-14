#!/usr/bin/env python3
""" This module defines the asynchronous routine: measure time."""
import time
import importlib
import asyncio

# Dynamically import wait_n from the 1-concurrent_coroutines module
wait_n = importlib.import_module('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for calling wait_n(n, max_delay)
    and returns the average time per function call.

    Args:
        n (int): The number of calls to wait_n.
        max_delay (int): The maximum delay in each call.

    Returns:
        float: The average time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))  # Run the coroutine with asyncio
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
