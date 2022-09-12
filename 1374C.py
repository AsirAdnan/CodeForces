for i in range(int(input())):
    input()
    a=input()
    o=0
    c=0
    for i in a:
        if i=='(':
            o+=1
        else:
            o-=1
        if o<0:
            o=0
            c+=1
    print(c)
