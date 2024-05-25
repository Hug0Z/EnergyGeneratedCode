from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element
    found until a given moment in the sequence.

    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    rolling_max_list = [numbers[0]]  # Start with the first element as the rolling max

    for i in range(1, len(numbers)):
        rolling_max_list.append(
            max(rolling_max_list[-1], numbers[i])
        )  # Append the maximum of current and previous max

    return rolling_max_list


# Example usage
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
