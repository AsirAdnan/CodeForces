for i in range(int(input())):
    input()
    a=list(map(int,input().split()))
    x=min(a)
    s=0
    for i in a:
        s+=abs(x-i)
    print(s)
