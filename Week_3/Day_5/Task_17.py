import timeit
import requests
import asyncio
import multiprocessing  # Add this import
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def timer(number, repeat):
    def wrapper(func):
        runs = timeit.repeat(func, number=number, repeat=repeat)
        print(sum(runs) / len(runs))
    return wrapper


@timer(1, 5)
def synchronous_sum():
    numbers = list(range(1000000))
    result = sum(numbers)
    print("Synchronous sum:", result)


@timer(1, 5)
def multithreading_sum():
    def thread_sum(numbers, result):
        result[0] = sum(numbers)

    numbers = list(range(1000000))
    result = [0]
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(thread_sum, numbers, result)
                   for _ in range(100)]
        for future in futures:
            future.result()
    print("Multithreading sum:", result[0])


@timer(1, 5)
def multiprocessing_sum():
    def process_sum(numbers, result_queue):
        result_queue.put(sum(numbers))

    numbers = list(range(1000000))
    result_queue = multiprocessing.Queue()
    with ProcessPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(
            process_sum, numbers, result_queue) for _ in range(100)]
        for future in futures:
            future.result()
    result = result_queue.get()
    print("Multiprocessing sum:", result)


@timer(1, 5)
def asynchronous_sum():
    async def async_sum():
        numbers = list(range(1000000))
        total = sum(numbers)
        return total

    async def gather_results():
        tasks = [async_sum() for _ in range(100)]
        results = await asyncio.gather(*tasks)
        print("Asynchronous sum:", sum(results))

    asyncio.run(gather_results())


if __name__ == "__main__":
    synchronous_sum()
    multithreading_sum()
    multiprocessing_sum()
    asynchronous_sum()
