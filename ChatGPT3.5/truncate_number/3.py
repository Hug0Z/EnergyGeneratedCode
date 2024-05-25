def truncate_number(number: float) -> float:
    """Return the decimal part of the number."""
    integer_part = int(number)  # Get the integer part of the number
    decimal_part = number - integer_part  # Calculate the decimal part
    return decimal_part
