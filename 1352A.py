for i in range(int(input())):
    a=int(input())
    l=[]
    for j in range(1,len(str(a))):
        x=int('1'+'0'*j)
        if a%x!=0:
            l.append(str(a%x))
            a-=a%x
    l.append(str(a))
    print(len(l))
    print(' '.join(l))
