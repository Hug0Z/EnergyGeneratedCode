from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """Generate a list of rolling maximum elements found until a given moment in the sequence."""
    max_numbers = []
    current_max = float("-inf")

    for num in numbers:
        current_max = max(current_max, num)
        max_numbers.append(current_max)

    return max_numbers


# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
