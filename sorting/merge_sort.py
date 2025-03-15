def merge_sort(numbers):
  if len(numbers) <= 1:
    return numbers

  mid = len(numbers) // 2
  left = merge_sort(numbers[:mid])
  right = merge_sort(numbers[mid:])

  return merge(left, right)


def merge(left, right):
  merged = []
  i, j = 0, 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1

  merged.extend(left[i:])
  merged.extend(right[j:])
  return merged
