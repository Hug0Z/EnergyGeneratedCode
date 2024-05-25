from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:  # If the list is empty, return it as is
        return numbers

    result = [
        numbers[0]
    ]  # Initialize the result list with the first element of numbers
    for num in numbers[1:]:  # Iterate over the remaining elements of numbers
        result.append(delimiter)  # Append the delimiter
        result.append(num)  # Append the current number

    return result


# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
