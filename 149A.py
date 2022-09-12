k=int(input())
a=list(map(int,input().split()))
s=0
c=0
a.sort(reverse=True)
for i in a:
    if s>=k:
        break
    else:
        s+=i
        c+=1
if s<k:
    print(-1)
else:
    print(c)
