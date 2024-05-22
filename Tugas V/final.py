import customtkinter as ctk

def execute():
    line = []
    req = []
    goto_command = []
    choosen_goto = []

    while True:
        text = textbox.get("1.0", "end-1c")  # Get the text from the textbox
        if "output" in text:
            break
        elif "jika" in text:
            req.append(text)
        elif "goto" in text:
            req.append(text)
        elif "cetak" in text:
            req.append(text)
        elif "=" in text:
            line.append(text)
        elif ":" in text:
            goto_command.append(text)

    var = {}

    for text in line:
        var_name, exp_to_eval = text.split('=')
        var_name = var_name.strip()
        exp_to_eval = exp_to_eval.strip()
        hasil_eval = eval(exp_to_eval, var)
        var[var_name] = hasil_eval

    left_part = None
    right_part = None

    for t in req:
        sub_part = t.split()
        if len(sub_part) == 2:
            left_part = sub_part[0].strip()
            right_part = sub_part[1].strip()
            result_hasil_eval = eval(right_part, var)
            var[right_part] = result_hasil_eval

        elif len(sub_part) == 4:
            left_part = sub_part[0].strip()
            declare_subpart = sub_part[1].strip()
            codevar_subpart = sub_part[2].strip()
            code_subpart = sub_part[3].strip()

        elif len(sub_part) == 5:
            left_part = sub_part[0].strip()
            declare_subpart = sub_part[1].strip()
            codevar_moresubpart = sub_part[2].strip()
            code_moresubpart = sub_part[3].strip()
            cadangan_subpart = sub_part[4].strip()

        if left_part == 'jika':
            print("masuk ke jika")
            if declare_subpart.find('>=') != -1:
                morepart = declare_subpart.split('>=')
                left_morepart = morepart[0]
                right_morepart = morepart[1]
                contain = var[left_morepart] 
                banding = contain >= int(right_morepart)
                print ("ini tanda banding >=", banding)

            elif declare_subpart.find('<=') != -1:
                morepart = declare_subpart.split('<=')
                left_morepart = morepart[0]
                right_morepart = morepart[1]
                contain = var[left_morepart] 
                banding = contain <= int(right_morepart)
                print ("ini tanda banding <=", banding)
                
            elif declare_subpart.find('<') != -1:
                morepart = declare_subpart.split('<')
                left_morepart = morepart[0]
                right_morepart = morepart[1]
                contain = var[left_morepart] 
                banding = contain < int(right_morepart)
                print ("ini tanda banding <", banding)
                
            elif declare_subpart.find('>') != -1:
                morepart = declare_subpart.split('>')
                left_morepart = morepart[0]
                right_morepart = morepart[1]
                contain = var[left_morepart] 
                banding = contain >int(right_morepart) 
                print ("ini tanda banding >", banding)


            elif declare_subpart.find('==') != -1:
                morepart = declare_subpart.split('==')
                left_morepart = morepart[0]
                right_morepart = morepart[1]
                contain = var[left_morepart] 
                banding = contain == int(right_morepart)
                print ("ini tanda banding ==", banding)

            elif declare_subpart.find('!=') != -1:
                morepart = declare_subpart.split('!=')
                left_morepart = morepart[0]
                right_morepart = morepart[1]
                contain = var[left_morepart] 
                banding = contain != int(right_morepart)
                print ("ini tanda banding !=", banding)

            if len (sub_part) == 4:
                if banding:
                    left_part = codevar_subpart
                    print(left_part)
                    right_part = code_subpart
                    print(right_part)
                else: 
                    print("Declare tidak memenuhi")

            elif len (sub_part) == 5:
                if code_moresubpart == '=':
                    left_part = codevar_moresubpart
                    change = cadangan_subpart
                    renew = eval(change, var)
                    var[left_part] = renew

        if left_part == 'cetak':
            print("Mencetak", var[right_part])

app = ctk.CTk()
app.geometry("800x700")

label = ctk.CTkLabel(master=app, text="How to input:\n1. You can declare as 'a = 2' or 'b = a + 3' and any other\n2. You can use the command 'cetak' to print out and 'jika' with 'jika (the condition) (your command)\n3. To show the output, click the 'output' button", font=('Arial', 18))

textbox = ctk.CTkTextbox(master=app, height=10, width=50)
btn = ctk.CTkButton(master=app, text="Output", command=execute)

label.pack()
textbox.pack()
btn.pack()

app.mainloop()
