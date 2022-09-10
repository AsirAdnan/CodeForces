a=list(map(int,input().split()))
a.sort()
c=a[-1]-a[0]
x=a[1]-c
b=a[2]-c
print(x,b,c)
