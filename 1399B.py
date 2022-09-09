for i in range(int(input())):
    input()
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=min(a)
    y=min(b)
    c=0
    for i in range(len(a)):
        p=a[i]-x
        q=b[i]-y
        if p>q:
            c+=p
        else:
            c+=q
    print(c)
