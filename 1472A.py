for i in range(int(input())):
    w,h,n=list(map(int,input().split()))
    c=1
    while c<n:
        if w%2==0:
            c*=2
            w//=2
        elif h%2==0:
            c*=2
            h//=2
        else:
            break
    if c>=n:
        print('YES')
    else:
        print("NO")
