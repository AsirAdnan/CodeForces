a,b=[int(i) for i in input().split()]
p={}
for _ in range(b):
    x,y=[int(i) for i in input().split()]
    if x not in p:
        p[x]=y
    else:
        p[x]+=y
f=True
t=list(p.keys())
t.sort()
for i in t:
    if a>i:
        a+=p[i]
    else:
        f=False
        print('NO')
        break 
if f:
    print("YES")
