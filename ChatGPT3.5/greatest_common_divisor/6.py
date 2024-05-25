def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers a and b."""
    while b != 0:
        a, b = b, a % b
    return a


# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
