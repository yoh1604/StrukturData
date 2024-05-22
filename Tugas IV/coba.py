def Stack():
    a=[]
    return a  
def push(a,data):
    a.append(data)  
def pop(a):
    data = a.pop()
    return data  
def peek(a):
    return a[len(a)-1]      
def isEmpty(a):
    return a == []  
def size(a):
    return len(a)
   
def infixToPrefix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    a = Stack()
    prefixList = [] 
    tokenList = infixexpr.split()
    hasil=' '
    step = 0
    for token in tokenList:
        print('langkah ke - %d: ' % (step+1))
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            prefixList.append(token)
            print("karakter dibaca",token)
        elif token == '(':
            push(a,token)
            print("karakter dibaca",token)
        elif token == ')':
            topToken = pop(a)
            print("karakter dibaca",token)
            while topToken != '(':
                prefixList.append(topToken)
                topToken = a.pop()
                print("karakter dibaca",topToken)        
        else:
            while (not isEmpty(a)) and \
               (prec[peek(a)] >= prec[token]):
                  prefixList.append(a.pop())
            push(a,token)
        print("isi tumpukan",a)
        print("hasil notasi terbentuk",prefixList)
        step=step+1
    while not isEmpty(a):
        prefixList.append(a.pop())  
    return "Hasil = "+hasil.join(prefixList)  
print(infixToPrefix("( A + B ) * C - ( D - E ) * ( F + G )"))
print("----------------------------------------------------------------------------------")
print(infixToPrefix("A * B + C * D "))

def Stack():
 
    a=[]
    return a  
def push(a,data):
    a.append(data)
def pop(a):
    data = a.pop()
    return data  
def peek(a):
    return a[len(a)-1]      
def isEmpty(a):
    return a == []  
def size(a):
    return len(a)
   
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    a = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    hasil=' '
    step = 0
    for token in tokenList:
        print('langkah ke - %d: ' % (step+1))
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
            print("karakter dibaca",token)
        elif token == '(':
            push(a,token)
            print("karakter dibaca",token)
        elif token == ')':
            topToken = pop(a)
            print("karakter dibaca",token)
            while topToken != '(':
                postfixList.append(topToken)
                topToken = a.pop()
                print("karakter dibaca",topToken)                
        else:
            while (not isEmpty(a)) and \
               (prec[peek(a)] >= prec[token]):
                  postfixList.append(a.pop())
            push(a,token)
        print("isi tumpukan",a)
        print("hasil notasi terbentuk",postfixList)
        step=step+1
    while not isEmpty(a):
        postfixList.append(a.pop())  
    return "Hasil = "+hasil.join(postfixList)      
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print("----------------------------------------------------------------------------------")
print(infixToPostfix("A * B + C * D "))