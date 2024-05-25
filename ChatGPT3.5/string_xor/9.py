def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings consisting only of 1s and 0s.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        str: The result of XOR operation as a binary string.

    Examples:
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
