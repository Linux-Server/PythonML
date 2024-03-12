import asyncio
from time import perf_counter,sleep

# MS => Block2 => OS => Block => TS => Block
async def main():
    print("Main started")
    task1 = asyncio.create_task(async_one())
    task2 = asyncio.create_task(async_two())
    await task1
    await task2
    # await asyncio.sleep(2)
    print("Main finished")

async def async_one():
    print("One started")
    await asyncio.sleep(2)
    print("One finished")

async def async_two():
    print("Two started")
    await asyncio.sleep(2)
    print("Two finished")



start_time = perf_counter()

asyncio.run(main())

print(f"Time Consumed: {perf_counter() - start_time}")