from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimiter)
    # Remove the last delimiter if the input list is not empty
    if result:
        result.pop()
    return result


# Test cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
