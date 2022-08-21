a=[]
b=input()
if len(b)==2:
    print(0)
else:
    b=b[1:-1].split(', ')
    for i in b:
        if i not in a:
            a.append(i)
    print(len(a))
