from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    # This works perfectly as-is
    arr1.extend(arr2)
    return arr1


def pop_n(arr: List[int], n: int) -> List[int]:
    # Max ensures N is never negative if n > len(arr)
    N = max(0, len(arr) - n)
    return arr[:N]


def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    # Python's .insert() automatically appends if index > len(arr)
    arr.insert(index, element)
    # If your goal was to force append at the exact index with padding,
    # you would need a different approach, but standard insert handles bounds natively.
    return arr


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(append_elements([4, 3], [4, 5, 3]))    # Output: [4, 3, 4, 5, 3]

print(pop_n([1, 2, 3, 4, 5], 2))             # Output: [1, 2, 3]
print(pop_n([1, 2, 3, 4, 5], 6))             # Output: [] (Fixed)
print(pop_n([1, 2, 3, 4, 5], 5))             # Output: []

print(insert_at([1, 2, 3, 4, 5], 2, 6))      # Output: [1, 2, 6, 3, 4, 5]
print(insert_at([1, 2, 3, 4], 6, 5))         # Output: [1, 2, 3, 4, 5] (Fixed)
