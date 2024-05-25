from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Removing spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize variables
    stack = []
    result = []
    current_group = ""

    # Iterate through the characters in the string
    for char in paren_string:
        if char == "(":
            stack.append(char)
            current_group += char
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
                if not stack:
                    result.append(current_group)
                    current_group = ""
            else:
                raise ValueError("Invalid input: unbalanced parentheses")

    # Check if all parentheses are balanced
    if stack:
        raise ValueError("Invalid input: unbalanced parentheses")

    return result
