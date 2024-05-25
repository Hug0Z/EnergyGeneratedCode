from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# Test the function
if __name__ == "__main__":
    strings = ["abc", "bacd", "cde", "array"]
    substring = "a"
    filtered_strings = filter_by_substring(strings, substring)
    print(filtered_strings)
