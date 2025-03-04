import asyncio

async def sub_array_sum(array: list, start: int, end: int) -> float:
    return sum(array[start:end])

async def array_sum(array: list) -> float:
    arr_size = len(array)
    
    # Split the array into two halves
    half = arr_size // 2
    results = await asyncio.gather(
        sub_array_sum(array, 0, half),
        sub_array_sum(array, half, arr_size)
    )
    return sum(results)

async def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = await array_sum(arr)
    print(result)

# Python 3.7+
asyncio.run(main())