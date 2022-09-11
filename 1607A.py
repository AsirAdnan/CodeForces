for i in range(int(input())):
    a=input()
    b=input()
    j=a.index(b[0])
    s=0
    for i in range(1,len(b)):
        s+=abs(a.index(b[i])-j)
        j=a.index(b[i])
    print(s)
