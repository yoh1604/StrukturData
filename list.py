def cetak(l):
    cetak = []
    for f in l:
        if type(f) ==  int:
            print(f)
        else:
            return cetak

l = [1,2,[3,4,5],5,[7,[8,9],3]]