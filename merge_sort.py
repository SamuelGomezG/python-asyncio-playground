import asyncio

def merge(left: list[float], right: list[float]) -> list[float]:
  result = []
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    elif right[j] < left[i]:
      result.append(right[j])
      j += 1
    else:
      result.append(left[i])
      i += 1
      j += 1
  
  while i < len(left):
    result.append(left[i])
    i += 1
  
  while j < len(right):
    result.append(right[j])
    j += 1
  
  return result

async def merge_sort(array: list[float]) -> list[float]:
  if len(array) <= 1:
    return array
  half_size = len(array) >> 1
  left_sub = await merge_sort(array[0:half_size])
  right_sub = await merge_sort(array[half_size:len(array)])
  return merge(left_sub, right_sub)