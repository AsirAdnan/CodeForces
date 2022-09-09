for i in range(int(input())):
    a=list(map(int,input().split()))
    x=a.pop(0)
    c=0
    for i in a:
        if i>x:
            c+=1
    print(c)
