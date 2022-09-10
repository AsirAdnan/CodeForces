input()
a=list(map(int,input().split()))
i=a.index(max(a))
c=0
while i!=0:
    a[i-1],a[i]=a[i],a[i-1]
    i-=1
    c+=1
a.reverse()
i=a.index(min(a))
while i!=0:
    a[i-1],a[i]=a[i],a[i-1]
    i-=1
    c+=1
print(c)
