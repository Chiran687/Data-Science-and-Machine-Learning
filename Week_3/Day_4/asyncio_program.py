import aiohttp
from Week_3.Day_4.Example import timer
import asyncio

url = "https://httpbin.org/uuid"


async def fetch(session, url):
    async with session.get(url) as response:
        json_data = await response.json()
        print(json_data['uuid'])


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for _ in range(100)]
        await asyncio.gather(*tasks)


@timer(1, 1)
def run():
    asyncio.run(main())
