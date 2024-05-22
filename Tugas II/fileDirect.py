import os
def directfile(path):
    list = os.listdir(path)
    for t in list:
        fn = os.path.join(path,t)
        if os.path.isdir(fn):
            directfile(fn)
        else: 
            print("List", fn)

directfile("C:\\Users\ASUS\OneDrive\Documents\KULIAH")