from fastapi import FastAPI
import asyncio
from time import sleep,perf_counter

app = FastAPI()


@app.get("/")
def root():
    count = perf_counter()
    sleep(2)
    print(f"The consumption is : {perf_counter() - count}")
    return True

@app.get("/a")



async def roots():
    count = perf_counter()
    await asyncio.sleep(2)
    print(f"The consumption is : {perf_counter() - count}")
    return True