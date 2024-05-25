def truncate_number(number: float) -> float:
    """Extracts the decimal part of a positive floating-point number."""
    integer_part = int(number)  # Extract the integer part
    decimal_part = number - integer_part  # Extract the decimal part
    return decimal_part
