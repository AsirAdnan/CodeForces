n,k=[int(i) for i in input().split()]
m=(4*60)-k
c=0
for i in range(1,n+1):
    if (i*5)<=m:
        c+=1
        m-=(i*5)
    else:
        break
print(c)
