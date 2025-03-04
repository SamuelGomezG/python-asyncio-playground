import asyncio

async def sub_array_sum(array: list[float], start: int, end: int) -> float:
    s = 0
    for i in range(start, end):
        s += array[i]
    return s

async def array_sum(array: list[float]) -> float:
    arr_size = len(array)
    
    # Split the array into two halves
    half_size = arr_size >> 1
    partial_sums = await asyncio.gather(
        sub_array_sum(array, 0, half_size),
        sub_array_sum(array, half_size, arr_size)
    )
    return partial_sums[0] + partial_sums[1]