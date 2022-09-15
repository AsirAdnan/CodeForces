for i in range(int(input())):
    a,b,c=(map(int,input().split()))
    t=0
    if c==1:
        if a==b:
            print(3)
        elif a>b:
            print(2)
        else:
            print(1)
    else:
        t=abs(c-b)+c
        if t==a:
            print(3)
        elif t>a:
            print(1)
        else:
            print(2)
