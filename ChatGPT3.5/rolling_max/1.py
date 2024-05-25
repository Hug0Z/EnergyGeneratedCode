from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_numbers = []
    current_max = float("-inf")  # Initialize current_max with negative infinity
    for num in numbers:
        current_max = max(
            current_max, num
        )  # Update current_max with the maximum of current_max and the current number
        max_numbers.append(current_max)  # Append the current maximum to the list
    return max_numbers


print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
