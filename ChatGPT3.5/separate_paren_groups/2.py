from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    stack = []
    start = None

    for i, char in enumerate(paren_string):
        if char == "(":
            stack.append(i)
            if len(stack) == 1:
                start = i
        elif char == ")":
            if len(stack) == 1:
                groups.append(paren_string[start : i + 1])
                start = None
            stack.pop()

    return groups
