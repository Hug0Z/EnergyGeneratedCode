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
    for num in numbers[:-1]:
        result.extend([num, delimiter])
    if numbers:  # check if the list is not empty
        result.append(numbers[-1])
    return result


# Test cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
