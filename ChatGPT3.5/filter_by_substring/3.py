from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    filtered_strings = [string for string in strings if substring in string]
    return filtered_strings


# Example usage:
# strings = ['abc', 'bacd', 'cde', 'array']
# substring = 'a'
# filtered_list = filter_by_substring(strings, substring)
# print(filtered_list)
