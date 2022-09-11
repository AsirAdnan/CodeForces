for i in range(int(input())):
    a,b=(map(int,input().split()))
    x=min(a,b)
    y=max(a,b)
    z=y-x
    if z%10==0:
        print(z//10)
    else:
        print((z//10)+1)
