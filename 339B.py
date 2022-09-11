n,b=map(int,input().split())
x=list(map(int,input().split()))
j=1
s=0
for i in x:
    if i>j:
        s+=(i-j)
    elif j>i:
        s+=(n-j+i)
    j=i
print(s)
