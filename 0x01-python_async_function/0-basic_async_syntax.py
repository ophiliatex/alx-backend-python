#!/usr/bin/env python3
"""Async function"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Async function to wait a random number between 0 and max_delay"""

    rand = uniform(0, max_delay)

    await asyncio.sleep(rand)

    return rand
