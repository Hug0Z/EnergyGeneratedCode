from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_numbers = []
    max_number = float("-inf")  # Initialize max_number to negative infinity

    for num in numbers:
        max_number = max(
            max_number, num
        )  # Update max_number to the maximum of itself and the current number
        max_numbers.append(max_number)  # Append the current maximum to the result list

    return max_numbers


# Example usage
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
