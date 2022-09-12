for i in range(int(input())):
    x=list(map(int,input().split()))
    a,b=map(int,input().split())
    y=max(x)
    x=min(x)
    if a*2<b:
        print((y+x)*a)
    else:
        y-=x
        s=x*b
        print(s+(y*a))
