a=input()
b=input()
c=input()
if len(a)+len(b)!=len(c):
    print("NO")
else:
    d=a+b
    f=True
    for i in d:
        if c.count(i)!=d.count(i):
            f=False
            break
    if f:
        print("YES")
    else:
        print("NO")
