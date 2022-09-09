for i in range(int(input())):
    input()
    a=list(map(int,input().split()))
    l=[]
    c=0
    for i in range(len(a)):
        if i%2!=a[i]%2:
            f=False
            for j in l:
                if j%2==a[i]%2 and i%2==a[j]%2:
                    c+=1
                    l.remove(j)
                    f=True
                    break
            if f==False:
                l.append(i)
    if len(l)>0:
        print(-1)
    else:
        print(c)
