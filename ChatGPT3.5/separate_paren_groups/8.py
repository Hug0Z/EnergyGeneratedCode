from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
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
                raise ValueError("Unbalanced parentheses.")
        elif char == " ":
            continue
        else:
            raise ValueError("Invalid character found.")

    if stack:
        raise ValueError("Unbalanced parentheses.")

    return result
