import asyncio
from array_sum import array_sum

async def main():
    arr = [float(e) for e in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    result = await array_sum(arr)
    print(result)

# Python 3.7+
asyncio.run(main())