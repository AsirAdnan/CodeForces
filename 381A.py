input()
a=list(map(int,input().split()))
s=0
d=0
f=True
while len(a)>0:
    if a[-1]>a[0]:
        if f:
            s+=a[-1]
            f=False
        else:
            d+=a[-1]
            f=True
        a.remove(a[-1])
    else:
        if f:
            s+=a[0]
            f=False
        else:
            d+=a[0]
            f=True
        a.remove(a[0])
print(s,d)    
