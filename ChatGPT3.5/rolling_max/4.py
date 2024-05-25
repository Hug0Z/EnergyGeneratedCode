from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = []
    max_num = float("-inf")  # Initialize max_num as negative infinity

    for num in numbers:
        max_num = max(max_num, num)
        max_numbers.append(max_num)

    return max_numbers


# Test cases
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
