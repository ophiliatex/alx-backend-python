# Async Comprehension Project

This project demonstrates the use of asynchronous generators and comprehensions in Python. Below are the tasks and their implementations.

## Task 0: Async Generator

`0-async_generator.py`

A coroutine `async_generator` that loops 10 times, each time asynchronously waits for 1 second, then yields a random number between 0 and 10.

## Task 1: Async Comprehensions

`1-async_comprehension.py`

A coroutine `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator`.

## Task 2: Run time for four parallel comprehensions

`2-measure_runtime.py`

A coroutine `measure_runtime` that measures the runtime of executing `async_comprehension` four times in parallel using `asyncio.gather`.

## Usage

To run the tasks, you can use the provided `main.py` files or create your own scripts to import and execute the functions.

### Example

```sh
python3 0-main.py
python3 1-main.py
python3 2-main.py

Make sure to test each task by creating appropriate `main.py` files as shown in the project description to ensure your code works as expected. The examples provided in the task descriptions will help you verify the correct implementation of each function.
