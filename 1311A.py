for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    if a>b:
        if (a-b)%2==0:
            print(1)
        else:
            print(2)
    elif b>a:
        if (b-a)%2==0:
            print(2)
        else:
            print(1)
    else:
        print(0)
