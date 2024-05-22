import tkinter as tk
from postfix import evaluate_postfix, topostfix
# from tkinter import messagebox
# from operator import index, le
# from turtle import pen

i=0
var = {}
left_part = None
right_part = None

def evaluate(exp_eval):
    # print(exp_eval)
    for i in var : #untuk setiap label variabel
        if i in exp_eval : #jika label pada index tersebut ada terdapat di ekspresi math yang diinginkan
            print(exp_eval)
            exp_eval = exp_eval.replace(i, str(var[i]))

    # print(exp_eval)
    postfix_exp, result = topostfix(exp_eval)
    return result

# def evaluate(postfix_expression, var):
#     stack = []

#     for char in postfix_expression:
#         if char.isalnum():
#             if char in var:
#                 stack.append(var[char])
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

def execute():
    line = tex.get("1.0", "end-1c").split("\n")

    output = ''
    j = 0
    
    print(len(line))
    while j < len(line):
        text = line[j]
        # print(f"text = {text}")
        sub_part = text.split()
        # print(len(sub_part), sub_part)
        if len(sub_part) == 2: 
            left_part = sub_part[0].strip()
            right_part = sub_part[1].strip()
            result_hasil_eval = evaluate(right_part)
            var[right_part] = result_hasil_eval

        elif len (sub_part) == 4:
            left_part = sub_part[0].strip() #isinya 'jika'
            declare_subpart = sub_part[1].strip() #isinya misalkan a<3, dll. note: tidak boleh ada spasi
            codevar_subpart = sub_part[2].strip() #isinya 'cetak' / 'goto' / b
            code_subpart = sub_part[3].strip() #isinya 'apa' dalam perintah 'cetak/goto (apa)' / '='

        elif len (sub_part) == 5:
            left_part = sub_part[0].strip() #isinya 'jika'
            declare_subpart = sub_part[1].strip() #isinya misalkan a<3, dll. note: tidak boleh ada spasi
            codevar_moresubpart = sub_part[2].strip() #isinya b
            code_moresubpart = sub_part[3].strip() #isinya '='
            cadangan_subpart = sub_part[4].strip()

        if text.find('jika') != -1:
            # print("masuk ke jika")
            if declare_subpart.find('>=') != -1:
                morepart = declare_subpart.split('>=')
                left_morepart = morepart[0]
                right_morepart = morepart[1]
                contain = var[left_morepart] 
                if right_morepart.isdigit():
                    banding = contain >= int(right_morepart) 
                    print ("value tanda banding >=", banding)
                else:
                    contain2 = var[right_morepart]
                    banding = contain >= contain2
                    print ("value tanda banding >=", banding)
            elif declare_subpart.find('<=') != -1:
                morepart = declare_subpart.split('<=')
                left_morepart = morepart[0]
                right_morepart = morepart[1]
                contain = var[left_morepart] 
                if right_morepart.isdigit():
                    banding = contain <= int(right_morepart) 
                    print ("value tanda banding <=", banding)
                else:
                    contain2 = var[right_morepart]
                    banding = contain <= contain2
                    print ("value tanda banding <=", banding)
            elif declare_subpart.find('<') != -1:
                morepart = declare_subpart.split('<')
                left_morepart = morepart[0]
                right_morepart = morepart[1]
                # print ("left morepart", left_morepart)
                contain = var[left_morepart] 
                if right_morepart.isdigit():
                    banding = contain < int(right_morepart) 
                    print ("value tanda banding <", banding)
                else:
                    contain2 = var[right_morepart]
                    banding = contain < contain2
                    print ("value tanda banding <", banding)
            elif declare_subpart.find('>') != -1:
                morepart = declare_subpart.split('>')
                left_morepart = morepart[0]
                right_morepart = morepart[1]
                contain = var[left_morepart] 
                if right_morepart.isdigit():
                    banding = contain > int(right_morepart) 
                    print ("value tanda banding >", banding)
                else:
                    contain2 = var[right_morepart]
                    banding = contain > contain2 
                    print ("value tanda banding >", banding)

            elif declare_subpart.find('==') != -1:
                morepart = declare_subpart.split('==')
                left_morepart = morepart[0]
                right_morepart = morepart[1]
                contain = var[left_morepart] 
                if right_morepart.isdigit():
                    banding = contain == int(right_morepart) 
                    print ("value tanda banding == int", banding)
                else:
                    contain2 = var[right_morepart]
                    banding = contain == contain2
                    print ("value tanda banding == c2", banding)

            elif declare_subpart.find('!=') != -1:
                morepart = declare_subpart.split('!=')
                left_morepart = morepart[0]
                right_morepart = morepart[1]
                contain = var[left_morepart] 
                if right_morepart.isdigit():
                    banding = contain != int(right_morepart) 
                    print ("value tanda banding !=", banding)
                else:
                    contain2 = var[right_morepart]
                    banding = contain != contain2
                    print ("value tanda banding !=", banding)
            if len (sub_part) == 4:
                if banding:
                    left_part = codevar_subpart
                    # print(left_part)
                    right_part = code_subpart
                    # print(right_part)
                else: 
                    print("Declare tidak memenuhi")

            elif len (sub_part) == 5:
                if code_moresubpart == '=':
                    left_part = codevar_moresubpart
                    change = cadangan_subpart
                    renew = evaluate(change, var)
                    var[left_part] = renew
                    # print("left part", left_part, "var leftpart", var[left_part])


        if text.find('cetak') != -1:
            print ("Mencetak", result_hasil_eval)
            command_right = " ".join(part[1:])
            try:
                # result = eval(command_right, var)
                output += str(result_hasil_eval) + "\n"
            except (NameError, SyntaxError):
                output += command_right + "\n"
                print("ERROR")

        elif text.find('=') != -1:
            if len(sub_part) == 3:
                # print("masuk ke sama dengan", text)
                part = text.split('=')  
                # print("part", part)     
                var_name = part[0].strip()
                # print("var name", var_name)
                exp_to_eval = part[1].strip()
                # print("exp to eval", exp_to_eval)
                hasil_eval = evaluate(topostfix(exp_to_eval), var)
                var[var_name] = hasil_eval
            if len (sub_part) == 5:
                # print("masuk ke len 5", text)
                part = text.split('=')        
                var_name = codevar_moresubpart
                # print("var name", var_name)
                exp_to_eval = cadangan_subpart
                # print("exp to eval", exp_to_eval)
                hasil_eval = evaluate(exp_to_eval, var)

                var[var_name] = hasil_eval
        
        if text.find(':') != -1:
            # print ("masuk titik dua")
            command = text.split(':')
            label = command[0].strip()
            index_label = j
            # print(f"baris ketemu titik dua {line.index(text)}")
            # print(index_label)

        elif text.find('goto') != -1 and banding:
            # print ("masuk ke goto", index_label)
            j = index_label
            # print(i)
            

        j += 1
    
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("1.0", output)
    output_text.config(state="disabled")


mode = tk.Tk()

mode.geometry("800x700")
mode.title("Yohana_5024221012")

root = tk.Frame(mode)
root.pack()
    
label = tk.Label(root, text = "How to input:\n1. You can declare as 'a = 2' or 'b = a + 3' and any other\n2. You can use the command 'cetak' to print out and 'jika' with 'jika (the condition) (your command)'\n3. To show the output, click the 'output' button", justify="center", font =('Kango',10))
label.pack(padx=20, pady = 20)

tex = tk.Text(root, height = 10, font=('Calibri', 14, "bold"))
tex.pack()

output_button = tk.Button(root, text="Output", font=('Kango', 10), command=execute)
output_button.pack(padx=20,pady=20)


# Label untuk menampilkan hasil input
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

output_text = tk.Text(root, height=10, width=40, state="disabled")
output_text.pack()

mode.mainloop()