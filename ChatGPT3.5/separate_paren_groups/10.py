from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")  # Remove spaces
    groups = []
    stack = []  # Stack to keep track of open parentheses indices

    for i, char in enumerate(paren_string):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                start = stack.pop()
                groups.append(paren_string[start : i + 1])

    return groups
