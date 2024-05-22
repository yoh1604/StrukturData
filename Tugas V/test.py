
def list_operator(char):
    operators = "+-*/^"
    return char in operators

def priority(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/':
        return 2
    if operator == '^':
        return 3
    return 0

def topostfix(infix_expression):
    postfix = []
    stack = []

    for char in infix_expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  
        elif list_operator(char):
            while stack and priority(stack[-1]) >= priority(char):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

def evaluate_postfix(postfix_expression, dict_variables):
    stack = []

    for char in postfix_expression:
        if char.isalnum():
            if char in dict_variables:
                stack.append(dict_variables[char])
            else:
                stack.append(int(char))
        elif list_operator(char):
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)
            elif char == '^':
                stack.append(operand1 ** operand2)

    return stack[0]
