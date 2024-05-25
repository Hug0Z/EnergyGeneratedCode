from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    filtered_strings = [s for s in strings if substring in s]
    return filtered_strings


# Testing the function
if __name__ == "__main__":
    test_strings = ["abc", "bacd", "cde", "array"]
    test_substring = "a"
    print(filter_by_substring(test_strings, test_substring))
