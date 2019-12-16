import time
import urllib.request
import asyncio
from asyncio import FIRST_COMPLETED
from pprint import pprint
import aiohttp
import random
import pprint


URL = 'https://jsonplaceholder.typicode.com/posts'


async def fetch_async(sleep_delay):
    # async with aiohttp.request('GET', URL) as resp:
    #     json = await resp.json()
    await asyncio.sleep(sleep_delay)
    print(f'{sleep_delay:.6f}')


# USING AS_COMLETED
# async def async_run():
#     for task in asyncio.as_completed([fetch_async(i) for i in MAX_CLIENTS]):
#         await task

async def foo():
    done = 2
    sleep_delay = 0.01
    while done != 1 and sleep_delay > 0:
        tasks = [asyncio.create_task(fetch_async(sleep_delay)) for i in range(1,100)]
        done, pending = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)

        for t in tasks:
            try:
                t.cancel()
            except:
                pass

        # done = len(done)
        print(f"#{len(done)}")
        # print(sleep_delay)
        sleep_delay -= 0.00001
        done = len(done)




def loop_run():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(foo())
    loop.close()

loop_run()

