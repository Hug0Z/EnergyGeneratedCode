from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimiter)
    if result:
        result.pop()  # Remove the last delimiter
    return result


# Test cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
