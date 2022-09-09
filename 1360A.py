for i in range(int(input())):
    a,b=list(map(int,input().split()))
    if a<b:
        a*=2
    else:
        b*=2
    if a<b:
        print(b**2)
    else:
        print(a**2)
