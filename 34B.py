a,b=map(int,input().split())
x=list(map(int,input().split()))
x.sort()
s=0
for i in x:
    if i>=0 or b==0:
        break
    else:
        s+=abs(i)
        b-=1
print(s)
