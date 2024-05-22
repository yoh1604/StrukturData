def evaluate(exp_eval):
    # print(exp_eval)
    for i in var : #untuk setiap label variabel
        if i in exp_eval : #jika label pada index tersebut ada terdapat di ekspresi math yang diinginkan
            print(exp_eval)
            exp_eval = exp_eval.replace(i, str(var[i]))

    # print(exp_eval)
    postfix_exp, result = topostfix(exp_eval)
    return result