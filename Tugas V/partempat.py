line = []
req = []
goto_command = []
choosen_goto = []
i=0
var = {}


while True:
    text = input('Yoh Compiler ~ ')
    print (text.find ("="))
    if text == "output":
        break
    elif text.find('jika') != -1:
        req.append(text)
        i+=1
        print("req jika", req)

    elif text.find('goto') != -1:
        req.append(text)
        i+=1
        print ("req goto", req)

    elif text.find('cetak') != -1:
        req.append(text)
        i+=1
        print ("req cetak", req)

    elif text.find('=') != -1:
        line.append(text)
        i+=1
        print ("line", line)

    elif text.find(':') != -1:
        i+=1
        goto_command.append(text, i)
        print("goto command", goto_command)

print("line", line)


for text in line:
    # if text.find(':'):
    #     allpart = text.split(':')
    #     part = allpart[1]
        
    part = text.split('=')        
    if len(part) == 2:
        var_name = part[0].strip()
        exp_to_eval = part[1].strip()
        
        hasil_eval = eval(exp_to_eval, var)
        var[var_name] = hasil_eval
        # print("exp_to_eval", exp_to_eval)
        # print("hasil eval", hasil_eval)

left_part = None
right_part = None

for t in req:
    print (t)
    sub_part = t.split()
    if len(sub_part) == 2: 
        left_part = sub_part[0].strip()
        right_part = sub_part[1].strip()

        result_hasil_eval = eval(right_part, var)
        var[right_part] = result_hasil_eval
        # print (sub_part)
    elif len (sub_part) == 4:
        left_part = sub_part[0].strip() #isinya 'jika'
        declare_subpart = sub_part[1].strip() #isinya misalkan a<3, dll. note: tidak boleh ada spasi
        codevar_subpart = sub_part[2].strip() #isinya 'cetak' / 'goto' / b
        code_subpart = sub_part[3].strip() #isinya 'apa' dalam perintah 'cetak/goto (apa)' / '='
        #cadangan_subpart = sub_part[4].strip()

    elif len (sub_part) == 5:
        left_part = sub_part[0].strip() #isinya 'jika'
        declare_subpart = sub_part[1].strip() #isinya misalkan a<3, dll. note: tidak boleh ada spasi
        codevar_moresubpart = sub_part[2].strip() #isinya 'cetak' / 'goto' / b
        code_moresubpart = sub_part[3].strip() #isinya 'apa' dalam perintah 'cetak/goto (apa)' / '='
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
        print ("Mencetak", var[right_part])

    elif left_part == 'goto':
        