a,b=[int(i) for i in input().split()]
for i in range(b):
    c=str(a)
    if c[-1]=='0':
        c=c[:-1]
        a=int(c)
    else:
        a-=1
print(a)
