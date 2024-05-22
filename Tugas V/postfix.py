def topostfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def has_higher_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]

    def is_operator(char):
        return char in '+-*/'

    def is_operand(char):
        return char.isdigit() or char.isalpha()  # Updated to support multi-digit numbers or variables

    output = []
    stack = []

    for char in expression:
        if is_operand(char):
            print(char)
            output.append(char)
        elif char == '(':
            print(char)
            stack.append(char)
        elif char == ')':
            print(char)
            while stack and stack[-1] != '(':
                output.append(stack.pop())
                print(output)
            stack.pop()
            print(stack)
        elif is_operator(char):
            while stack and stack[-1] != '(' and has_higher_precedence(stack[-1], char):
                output.append(stack.pop())
                print(output)
            stack.append(char)
            print(stack)

    while stack:
        output.append(stack.pop())

    postfix_exp = ''.join(output)

    # Evaluate the postfix expression
    result = evaluate_postfix(postfix_exp)

    return postfix_exp, result

def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char in "+-*/":
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

    return stack[0]

def infix_with_bracket(expression):
    stack = []
    for char in expression:
        stack.append(char)
    return ''.join(stack)

exp = input("Masukkan infix: ")

print("Postfix Expression:")
postfix_exp, result = topostfix(exp)
print(postfix_exp)
print("Result of postfix expression:", result)
print("Infix With Brackets =", infix_with_bracket(postfix_exp))

# if __name__ == '__main__':
    # exp = input("Masukkan infix: ")
    
    # print("Postfix Expression:")
    # postfix_exp, result = infix_to_postfix(exp)
    # print(postfix_exp)
    # print("Result of postfix expression:", result)
    # print("Infix With Brackets =", infix_with_bracket(postfix_exp))
