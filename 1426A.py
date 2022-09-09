for _ in range(int(input())):
    a,x=list(map(int,input().split()))
    if a<=2:
        print(1)
    else:
        s=2
        n=1
        while s<a:
            s+=x
            n+=1
        print(n)
