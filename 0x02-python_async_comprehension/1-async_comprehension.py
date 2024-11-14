#!/usr/bin/env python3
"""
   This module defines the asychronous
   coroutine: async_comprehension.
"""
import importlib
import asyncio

# Import async_generator from the previous task using importlib
async_generator_module = importlib.import_module('0-async_generator')
async_generator = async_generator_module.async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator
    using an async comprehension, and returns them as a list.
    """
    return [number async for number in async_generator()]
