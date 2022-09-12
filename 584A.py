n,t=map(int,input().split())
s=int('1'+'0'*(n-1))
p=int('9'*n)
f=False
for i in range(s,p+1):
    if i%t==0:
        f=True
        break
if f:
    print(i)
else:
    print(-1)
