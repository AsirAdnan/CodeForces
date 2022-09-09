for i in range(int(input())):
    a=list(map(int,input().split()))
    w,x,y,z=a
    p=max(w,x)
    q=max(y,z)
    a.sort(reverse=True)
    if max(p,q)==a[0] and min(p,q)==a[1]:
        print("YES")
    else:
        print("NO")
