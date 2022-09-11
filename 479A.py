a=int(input())
b=int(input())
c=int(input())
if a==b==c==1:
    print(3)
elif a==b==1:
    print(2*c)
elif a==c==1:
    print(2+b)
elif b==c==1:
    print(2*a)
elif a==1:
    print((a+b)*c)
elif b==1:
    if c>a:
        print((a+b)*c)
    else:
        print(a*(b+c))
elif c==1:
    print(a*(b+c))
else:
    print(a*b*c)
