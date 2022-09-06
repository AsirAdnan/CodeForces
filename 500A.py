x=input().split()
x=int(x[-1])
a=[int(i) for i in input().split()]
t=1
f=False
for i in range(len(a)):
    t+=a[t-1]
    if t==x:
        f=True
        break
    if t>x or t-1>len(a):
        break
if f:
    print('YES')
else:
    print('NO')
