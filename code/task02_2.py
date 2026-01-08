from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    results = []
    groups = paren_string.split()
    for group in groups:
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        results.append(max_depth)
    return results