from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize variables
    groups = []
    current_group = ""
    balance = 0

    # Iterate through the characters in the string
    for char in paren_string:
        if char == "(":
            # Increment the balance when an open parenthesis is encountered
            balance += 1
            # Add the character to the current group
            current_group += char
        elif char == ")":
            # Decrement the balance when a closing parenthesis is encountered
            balance -= 1
            # Add the character to the current group
            current_group += char
            if balance == 0:
                # If balance becomes zero, it indicates a complete group
                groups.append(current_group)
                # Reset the current_group for the next group
                current_group = ""
        else:
            # Ignore any characters that are not parentheses
            pass

    return groups
