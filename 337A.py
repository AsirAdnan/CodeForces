a=int(input().split()[0])
b=list(map(int,input().split()))
b.sort()
m=sum(b)
for i in range(len(b)-a+1):
    if abs(b[i+a-1]-b[i])<m:
        m=abs(b[i+a-1]-b[i])
print(m)
