
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

def infix_to_postfix(infix_expression):
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

# def evaluate_postfix(postfix_expression, dict_variables):
#     stack = []

#     for char in postfix_expression:
#         if char.isalnum():
#             if char in dict_variables:
#                 stack.append(dict_variables[char])
#             else:
#                 stack.append(int(char))
#         elif list_operator(char):
#             operand2 = stack.pop()
#             operand1 = stack.pop()
#             if char == '+':
#                 stack.append(operand1 + operand2)
#             elif char == '-':
#                 stack.append(operand1 - operand2)
#             elif char == '*':
#                 stack.append(operand1 * operand2)
#             elif char == '/':
#                 stack.append(operand1 / operand2)
#             elif char == '^':
#                 stack.append(operand1 ** operand2)

#     return stack[0]


# def operation(line):
#     operators = ["+", "-", "*", "/"]
#     for operator in operators:
#         if operator in line:
#             return True, operator
#     return False, None


# def eval(operand1, operator, operand2):
#     operand1 = int(operand1)
#     operand2 = int(operand2)
#     if operator == "+":
#         return operand1 + operand2
#     elif operator == "-":
#         return operand1 - operand2
#     elif operator == "*":
#         return operand1 * operand2
#     elif operator == "/":
#         return operand1 / operand2
#     else:
#         return None


# # Set buat operator
# operators = set(['+', '-', '*', '/', '(', ')', '^'])
# # Kedudukan operator, pake dictionary
# precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

# # Fungsi buat konversi infix to postfix
# def InfixToPostfix(inputExpression):
#     stack = []
#     output = ''
#     temp = ''
    
#     for character in inputExpression:
#         if character.isdigit():
#             temp += character
#         elif character.isalnum():
#             temp += character
#         else:
#             if temp:
#                 output += temp + ' '
#                 temp = ''
#             if character == '(':
#                 stack.append(character)
#             elif character == ')':
#                 while stack and stack[-1] != '(':
#                     output += stack.pop() + ' '
#                 stack.pop()
#             elif character in operators:
#                 while stack and stack[-1] != '(' and precedence.get(character, 0) <= precedence.get(stack[-1], 0):
#                     output += stack.pop() + ' '
#                 stack.append(character)
    
#     if temp:
#         output += temp + ' '
        
#     while stack:
#         output += stack.pop() + ' '
        
#     return output

# # Fungsi untuk menghitung hasil ekspresi postfix
# def evaluate(postfixExpression, dict_variables):
#     stack = []
    
#     for character in postfixExpression.split():
        
#         if character.isalnum():
#             if character in dict_variables:
#                 stack.append(int(dict_variables[character]))
#         if character.isdigit():
#             stack.append(int(character))
#         elif character in operators:
#             if len(stack) < 2:
#                 print("Error: Tidak ada cukup operan untuk operasi", character)
#                 return None

#             operand2 = stack.pop()
#             operand1 = stack.pop()
#             if character == '+':
#                 result = operand1 + operand2
#             elif character == '-':
#                 result = operand1 - operand2
#             elif character == '*':
#                 result = operand1 * operand2
#             elif character == '/':
#                 result = operand1 / operand2
#             elif character == '^':
#                 result = operand1 ** operand2
#             stack.append(result)
            
#         if character in operators:
#             print(f'Evaluating: Operator: {character}, Stack: {stack}')
#         else:
#             print(f'Evaluating: Operand: {character}, Stack: {stack}')

#     if len(stack) != 1:
#         print("Error: Ekspresi postfix tidak valid")
#         return None

#     # Hasil akhir evaluasi ada di puncak stack
#     return stack[0]

# # Fungsi konversi ekspresi postfix jadi ekspresi infix
# def PostfixToInfix(postfixExpression):
#     stack = []
#     n = 0

#     # Fungsi untuk menentukan apakah karakter adalah operator
#     def isOperator(char):
#         return char in operators

#     # Fungsi untuk menggabungkan dua ekspresi infix dengan operator yang sesuai
#     def CombineOperands(op1, op2, operator):
#         return f"({op1}{operator}{op2})"

#     for character in postfixExpression.split():
#         if character.isdigit():  # Jika karakter adalah angka
#             stack.append(character)  # Masukkan angka ke stack
#         elif isOperator(character):
#             operand2 = stack.pop()
#             operand1 = stack.pop()
#             infix_expression = CombineOperands(operand1, operand2, character)
#             stack.append(infix_expression)

#             n += 1
#             print(f"Step {n}: {infix_expression}")

#     return stack[0]
