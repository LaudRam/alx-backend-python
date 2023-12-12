#!/usr/bin/env python3
'''
    Import async_comprehension and write a measure_runtime
    coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Measures the total runtime and return it '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
