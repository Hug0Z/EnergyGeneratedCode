from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    max_depth = 0
    current_depth = 0

    for char in paren_string:
        if char == "(":
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ")":
            current_depth -= 1
        elif char == " ":
            depths.append(max_depth)
            max_depth = 0

    depths.append(max_depth)  # To account for the last group

    return depths


# Test the function
print(parse_nested_parens("(()()) ((())) () ((())()())"))  # Output: [2, 3, 1, 3]
