def postfix(mathExpress):
    order = {}
    order ["("] = 1
    order ["*"] = 2
    order ["/"] = 2
    order ["+"] = 3
    order ["-"] = 3

    operatorStack = []
    outputPostfix = []
    currentNumber = []

    for r in mathExpress:
        if r.isalnum():
            currentNumber.append(r)
        elif r in order:
            if currentNumber:
                outputPostfix.append(''.join(currentNumber))
                currentNumber = []
            while (operatorStack and operatorStack[-1] in order and
                   order[r] <= order[operatorStack[-1]]):
                outputPostfix.append(operatorStack.pop())
            operatorStack.append(r)
        elif r == '(':
            operatorStack.append(r)
        elif r == ')':
            if currentNumber:
                outputPostfix.append(''.join(currentNumber))
                currentNumber = []
            while (operatorStack and operatorStack[-1] != '('):
                outputPostfix.append(operatorStack.pop())
            if operatorStack and operatorStack[-1] == '(':
                operatorStack.pop()

    if currentNumber:
        outputPostfix.append(''.join(currentNumber))

    while operatorStack:
        outputPostfix.append(operatorStack.pop())

    return ' '.join(outputPostfix)

mathExpress = input("Masukkan Ekspresi Matematika:")
postfix_Expression = postfix(mathExpress)
print("Postfix Expression:", postfix_Expression)
