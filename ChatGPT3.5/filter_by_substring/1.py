from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings only for ones that contain given substring"""
    filtered_strings = [string for string in strings if substring in string]
    return filtered_strings


if __name__ == "__main__":
    # Test cases
    print(filter_by_substring([], "a"))  # []
    print(
        filter_by_substring(["abc", "bacd", "cde", "array"], "a")
    )  # ['abc', 'bacd', 'array']
