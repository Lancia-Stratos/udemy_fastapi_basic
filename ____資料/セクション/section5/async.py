import asyncio

async def async_function():
    print("hello")
    await asyncio.sleep(2)
    print("world")
    
asyncio.run(async_function())