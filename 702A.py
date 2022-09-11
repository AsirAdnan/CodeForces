input()
x=list(map(int,input().split()))
y=0
c=1
for i in range(len(x)-1):
    if x[i+1]<=x[i]:
        if c>y:
            y=c
        c=1
    else:
        c+=1
if c>y:
    print(c)
else:
    print(y)
