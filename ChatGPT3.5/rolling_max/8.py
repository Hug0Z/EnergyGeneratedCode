from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = []
    current_max = float("-inf")  # Start with negative infinity as the current maximum

    for num in numbers:
        current_max = max(current_max, num)  # Update the current maximum
        max_numbers.append(current_max)  # Append the current maximum to the result list

    return max_numbers


# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
