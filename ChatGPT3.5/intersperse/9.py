from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:  # Check if the list is empty
        return []

    result = [numbers[0]]  # Start with the first element
    for num in numbers[1:]:  # Iterate over the rest of the elements
        result.extend([delimiter, num])  # Add delimiter and the number
    return result
