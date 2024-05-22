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

infix = input("Masukkan INFIX: ")
for i in infix:
    if i not in operators and i != '(' and i != ')':
        output.append(i)
    elif i == '(':
        s.push(i)
    elif i == ')':
        while not s.isEmpty() and s.peek() != '(':
            output.append(s.pop())
        s.pop() 
    elif i in operators:
        while not s.isEmpty() and prior[i] <= prior.get(s.peek(), 0):
            output.append(s.pop())
        s.push(i)
    print ('stack:', s.items, 'output:', output)

while not s.isEmpty():
    output.append(s.pop())
    
print('POSTFIX:', ''.join(output))