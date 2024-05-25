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
    # Remove the extra delimiter at the end if there are elements in the list
    if result:
        result.pop()
    return result
