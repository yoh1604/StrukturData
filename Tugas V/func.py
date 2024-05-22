import tkinter as tk
from tkinter import filedialog

dict_variables = {}
output = ""
syarat_goto = None

def open_notepad():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            input_text.delete("1.0", "end")
            input_text.insert("1.0", content)

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


def process_inputs(user_inputperline, current_line):
    global output, syarat_goto
    print ("user input " + user_inputperline)
    parts = user_inputperline.split()
    print(f"parts = {parts}")
    print(f"syarat_goto = {syarat_goto}")

    if '=' in parts:
        loc_equal = parts.index('=')
        variable = parts[loc_equal - 1]
        expression_to_evaluate = parts[loc_equal + 1]
        result = evaluate_postfix(infix_to_postfix(expression_to_evaluate), dict_variables)
        dict_variables[variable] = result
        print("variabel=" + variable)
        print("persamaan=" + ' '.join(expression_to_evaluate))
        print("hasil" + str(result))

    if 'cetak' in parts:
        loc_cetak = parts.index('cetak')
        command_cetak = parts[loc_cetak + 2:-1]
        print(command_cetak)
        try:
            result = evaluate_postfix(infix_to_postfix(command_cetak), dict_variables)
            print(result)
            output += str(result) + "\n"
        except:
            output += str(' '.join(command_cetak[0:])) + "\n"
    
    if 'syarat:' in parts:
            syarat_goto = current_line
            print (f"syarat_goto = {syarat_goto}")
            
    if 'jika' in parts:
        loc_jika = parts.index('jika')
        exp_jika = parts [loc_jika + 1]
        print (exp_jika)
        if '==' in exp_jika:
            pisahin = exp_jika.split('==')
            left = dict_variables[pisahin [0]]
            right = pisahin [1]
            print(left)
            print(right)
            if int(left) == int(right):
                print("oke")
                if parts [loc_jika +2] == 'cetak':
                    perintah = parts[loc_jika +3]
                    print ("ayo")
                    try:
                        result = evaluate_postfix(infix_to_postfix(perintah), dict_variables)
                        print(result)
                        output += str(result) + "\n"
                    except:
                        output += str(' '.join(command_cetak[0:])) + "\n"
                elif parts [loc_jika +2] == 'goto':
                      print("print cek goto")
                      goto_index = parts.index("goto")
                      check_point = parts[goto_index + 1]
                      return check_point
                   
        if '>' in exp_jika:
            pisahin = exp_jika.split('>')
            left = dict_variables[pisahin [0]]
            right = pisahin [1]
            print(left)
            print(right)
            if int(left) > int(right):
                print("oke")
                if parts [loc_jika +2] == 'cetak':
                    perintah = parts[loc_jika +3]
                    print ("ayo")
                    try:
                        result = evaluate_postfix(infix_to_postfix(perintah), dict_variables)
                        print(result)
                        output += str(result) + "\n"
                    except:
                        output += str(' '.join(command_cetak[0:])) + "\n"
                elif parts [loc_jika +2] == 'goto':
                      print("print cek goto")
                      goto_index = parts.index("goto")
                      check_point = parts[goto_index + 1]
                      return check_point
        if '<' in exp_jika:
            pisahin = exp_jika.split('<')
            left = dict_variables[pisahin [0]]
            right = pisahin [1]
            if int(left) < int(right):
                print("oke")
                if parts [loc_jika +2] == 'cetak':
                    perintah = parts[loc_jika +3]
                    print ("ayo")
                    try:
                        result = evaluate_postfix(infix_to_postfix(perintah), dict_variables)
                        print(result)
                        output += str(result) + "\n"
                    except:
                        output += str(' '.join(command_cetak[0:])) + "\n"
                elif parts [loc_jika +2] == 'goto':
                      print("print cek goto")
                      goto_index = parts.index("goto")
                      check_point = parts[goto_index + 1]
                      return check_point
        
        

       
def run_compiler():
    global output, syarat_goto
    lines = input_text.get("1.0", "end-1c").split("\n")
    print(lines)

    output = ""

    i = 0
    while i < len(lines):
        var = process_inputs(lines[i], i)

        if var == 'syarat':
            if syarat_goto != None:
                i = syarat_goto

        i = i + 1

    # supaya keluar output di window
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("1.0", output)
    output_text.config(state="disabled")

# window
window = tk.Tk()
window.title("Larguage")

frame = tk.Frame(window)
frame.pack()

# tambahkan tombol untuk membuka Notepad
open_notepad_button = tk.Button(frame, text="Open Notepad", command=open_notepad)
open_notepad_button.pack()

# bagian input
input_label = tk.Label(frame, text="Masukkan kode:")
input_label.pack()

input_text = tk.Text(frame, height=10, width=40)
input_text.pack()

# tombol compile
compile_button = tk.Button(frame, text="RUN", command=run_compiler)
compile_button.pack()

# bagian output
output_label = tk.Label(frame, text="Output:")
output_label.pack()

output_text = tk.Text(frame, height=10, width=40, state="disabled")
output_text.pack()

window.mainloop()