from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    result = []
    current_group = ""

    for char in paren_string:
        if char == "(":
            stack.append("(")
            current_group += char
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
                if not stack:
                    result.append(current_group)
                    current_group = ""
            else:
                # If stack is empty and encountering closing parenthesis,
                # it indicates an unbalanced parenthesis sequence.
                raise ValueError("Unbalanced parentheses")
        else:
            # Ignore any non-parenthesis characters
            continue

    if stack:
        # If stack is not empty after parsing all characters,
        # it indicates an unbalanced parenthesis sequence.
        raise ValueError("Unbalanced parentheses")

    return result
