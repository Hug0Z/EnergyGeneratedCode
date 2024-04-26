from typing import List 

# def parse_nested_parens(paren_string: str) -> List[int]: 
#     """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces. For each of the group, output the deepest level of nesting of parentheses. E.g. (()()) has maximum two levels of nesting while ((())) has three. >>> parse_nested_parens('(()()) ((())) () ((())()())') [2, 3, 1, 3] """ 

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    >>> parse_nested_parens('(()()) ((())) () ((())()())') [2, 3, 1, 3]
    """
    result = []
    stack = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(char)
    while len(stack) > 0:
        result.append(len(stack))
        stack.pop()
    return result