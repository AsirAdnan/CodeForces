r,b=[int(i) for i in input().split()]
f=0
c=0
while r+b>=2:
    if r>0 and b>0:
        f+=1
        r-=1
        b-=1
    else:
        if r>=2:
            r-=2
            c+=1
        elif b>=2:
            b-=2
            c+=1
print(f,c)
