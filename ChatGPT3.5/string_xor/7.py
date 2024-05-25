from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    >>> string_xor('010', '110')
    '100'
    """
    result = ""
    for char1, char2 in zip(a, b):
        if char1 != char2:
            result += "1"
        else:
            result += "0"
    return result


# Test the function
print(string_xor("010", "110"))  # Output: '100'
