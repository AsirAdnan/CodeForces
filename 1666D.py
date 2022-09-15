for i in range(int(input())):
    a,b=input().split()
    c=[]
    for i in a:
        if i not in c:
            c.append(i)
            temp=a.count(i)-b.count(i)
            if temp<0:
                break
            else:
                for j in range(temp):
                    y=a.find(i)
                    a=a[:y]+a[y+1:]
    if a==b:
        print('YES')
    else:
        print('NO')
