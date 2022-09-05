s,m=[int(i) for i in input().split()]
c=1
while s!=0:
    s-=1
    if c%m==0:
        s+=1
    if s==0:
        break
    else:
        c+=1
print(c)
