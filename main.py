import random
import asyncio
from array_sum import array_sum
from merge_sort import merge_sort

async def main():
    arr = [float(e) for e in range(1, 101)]
    result = await array_sum(arr)
    print(result)
    
    random.shuffle(arr)
    sorted_arr = await merge_sort(arr)
    print(arr)
    print(sorted_arr)

# Python 3.7+
asyncio.run(main())