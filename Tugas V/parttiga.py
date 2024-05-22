from operator import index, le
from turtle import pen
import postfix

line = []
goto_command = []
choosen_goto = []
i=0
j = 0
var = {}
left_part = None
right_part = None

while True:
    text = input('Yoh Compiler ~ ')
    if text == 'output':
        break
    else:
        line.append(text)
        i += 1
        # print("Isi Line", line, "Index ke - ", i)

print(len(line))
while j < len(line):
    text = line[j]
    # print(f"text = {text}")
    sub_part = text.split()
    # print(len(sub_part), sub_part)
    if len(sub_part) == 2: 
        print("harusnya masuk eval dua part")
        left_part = sub_part[0].strip()
        right_part = sub_part[1].strip()
        result_hasil_eval = postfix(right_part, var)
        print ("bukan yang ini", result_hasil_eval)
        var[right_part] = result_hasil_eval
        print ("yangini", var_name)

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
                renew = postfix(change, var)
                var[left_part] = renew
                # print("left part", left_part, "var leftpart", var[left_part])


    if text.find('cetak') != -1:

        print ("Mencetak", result_hasil_eval)

    elif text.find('=') != -1:
        if len(sub_part) == 3:
            print("masuk ke sama dengan", text)
            part = text.split('=')  
            print("part", part)     
            var_name = part[0].strip()
            print("var name", var_name)
            exp_to_eval = part[1].strip()
            print("exp to eval", exp_to_eval)
            hasil_eval = postfix(exp_to_eval, var)
            var[var_name] = hasil_eval
        if len (sub_part) == 5:
            # print("masuk ke len 5", text)
            part = text.split('=')        
            var_name = codevar_moresubpart
            # print("var name", var_name)
            exp_to_eval = cadangan_subpart
            # print("exp to eval", exp_to_eval)
            hasil_eval = eval(exp_to_eval, var)
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