import re

def evaluate_expression(expr, variables, operators):
    """
    Evaluates a mathematical expression with custom operators and variables.

    Args:
        expr: The expression string to evaluate.
        variables: A dictionary mapping variable names to their integer values.
        operators: A dictionary mapping operator symbols to (precedence, function) tuples.

    Returns:
        The integer result of evaluating the expression.
    """

    token_pattern = re.compile(r'(\d+|[a-z]|\(|\)|\S)')
    tokens = [t for t in token_pattern.findall(expr) if not t.isspace()]

    output_queue = []
    operator_stack = []

    # Shunting-Yard Algorithm to convert infix to Reverse Polish Notation (RPN)
    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            output_queue.append(int(token))
        elif token.islower():
            output_queue.append(variables.get(token, 0))
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()  # Pop '('
        elif token in operators:
            op_prec, _ = operators[token]
            # Pop operators from stack with higher or equal precedence
            while (operator_stack and operator_stack[-1] in operators and
                   operators[operator_stack[-1]][0] >= op_prec):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)

    while operator_stack:
        output_queue.append(operator_stack.pop())

    # RPN Evaluation
    eval_stack = []
    for token in output_queue:
        if isinstance(token, int):
            eval_stack.append(token)
        elif token in operators:
            op_func = operators[token][1]
            right_operand = eval_stack.pop()
            left_operand = eval_stack.pop()
            eval_stack.append(op_func(left_operand, right_operand))

    return eval_stack[0]