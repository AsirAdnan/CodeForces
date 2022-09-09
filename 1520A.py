for i in range(int(input())):
    l=[]
    input()
    a=input()
    s=a[0]
    f=True
    for i in a:
        if i!=s:
            if i in l:
                f=False
                print("NO")
                break
            else:
                l.append(s)
                s=i
    if f:
        print("YES")
