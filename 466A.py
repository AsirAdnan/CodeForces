n,m,a,b=[int(i) for i in input().split()]
if (a<(b/m)):
    print(n*a)
else:
    x=n//m
    p=(b*(n//m))
    n=n%m
    if (n*a)<b:
        print(p+(n*a))
    else:
        print(p+b)
