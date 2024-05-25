from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []

    max_seen = numbers[0]
    rolling_max_list = [max_seen]

    for num in numbers[1:]:
        if num > max_seen:
            max_seen = num
        rolling_max_list.append(max_seen)

    return rolling_max_list


# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output should be [1, 2, 3, 3, 3, 4, 4]
