def postfix(mathExpress):
    class Stack:
        def _init_(self):
            self.items = []
        def isEmpty(self):
            return len(self.items) == 0
        def push(self, item):
            self.items.append(item)
        def pop(self):
            if not self.isEmpty():
                return self.items.pop()
        def peek(self):
            if not self.isEmpty():
                return self.items[-1]
        def getSize(self):
            return len(self.items)

    output = []
    operators = {'+', '-', '*', '/', '^'}
    prior = {}
    prior['+'] = 1
    prior['-'] = 1
    prior['*'] = 2
    prior['/'] = 2
    prior['^'] = 3

    s = Stack()

    for i in mathExpress:
        if i not in operators and i != '(' and i != ')':
            output.append(i)
        elif i == '(':
            s.push(i)
        elif i == ')':
            while not s.isEmpty() and s.peek() != '(':
                output.append(s.pop())
            s.pop(i) 
        elif i in operators:
            while not s.isEmpty() and prior[i] <= prior.get(s.peek(), 0):
                output.append(s.pop())
            s.push(i)
        print ('stack:', s.items, 'output:', output)

    while not s.isEmpty():
        output.append(s.pop())
        
    print('POSTFIX:', ''.join(output))
    # order = {}
    # order ["("] = 1
    # order ["*"] = 2
    # order ["/"] = 2
    # order ["+"] = 3
    # order ["-"] = 3

    # operatorStack = []
    # outputPostfix = []

    # for r in mathExpress:
        
    #     if r.isalnum():
    #         outputPostfix.append(r)
    #     elif r in order:
    #         while (operatorStack and operatorStack[-1] in order and
    #                order[r] <= order[operatorStack[-1]]):
    #             outputPostfix.append(operatorStack.pop())
    #         operatorStack.append(r)
    #     elif r == '(':
    #         operatorStack.append(r)
    #     elif r == ')':
    #         while (operatorStack and operatorStack[-1] != '('):
    #             outputPostfix.append(operatorStack.pop())
    #         if operatorStack and operatorStack[-1] == '(':
    #             operatorStack.pop()
    #     print(outputPostfix)
    #     print(operatorStack)

    # while operatorStack:
    #     outputPostfix.append(operatorStack.pop())

    # print ("Infix to Postfix", outputPostfix)

    # return ''.join(outputPostfix)


# def prefix(mathExpress):
#     order = {}
#     order ["("] = 1
#     order ["*"] = 2
#     order ["/"] = 2
#     order ["+"] = 3
#     order ["-"] = 3

#     operatorStack = []
#     outputPrefix = []

#     for r in mathExpress:
        
#         if r.isalnum():
#             outputPrefix.append(r)
#         elif r == ')':
#             operatorStack.append(r)
#         elif r == '(':
#             while operatorStack and operatorStack[-1] != ')':
#                 outputPrefix.append(operatorStack.pop())
#             if operatorStack and operatorStack[-1] == ')':
#                 operatorStack.pop()
#         elif r in order:
#             while (operatorStack and operatorStack[-1] in order and
#                    order[r] < order[operatorStack[-1]]):
#                 outputPrefix.append(operatorStack.pop())
#             operatorStack.append(r)
#     print(outputPrefix)

#     while operatorStack:
#         outputPrefix.append(operatorStack.pop())

#     # print ("Infix to Postfix", outputPrefix)
#     return ''.join(outputPrefix[::-1])  # Reverse the result to get the prefix expression

# pilihan = input ("Postfix (1) or Prefix (2):")
mathExpress = input("Masukkan Ekspresi Matematika:")

postfix_Expression = postfix(mathExpress)
print("Postfix Expression:", postfix_Expression)
# if pilihan == '1': 
#     postfix_Expression = postfix(mathExpress)
#     print("Postfix Expression:", postfix_Expression)
# elif pilihan == '2': 
#     prefix_Expression = prefix(mathExpress)
#     print("Prefix Expression:", prefix_Expression)
# else:
#     print("Invalid choice.")
    