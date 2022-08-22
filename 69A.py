x=y=z=0
for i in range(int(input())):
    a,b,c=input().split()
    x+=(int(a))
    y+=int(b)
    z+=int(c)
if x==y==z==0:
    print("YES")
else:
    print("NO")
