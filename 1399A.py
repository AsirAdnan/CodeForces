for i in range(int(input())):
    input()
    a=list(map(int,input().split()))
    a.sort()
    f=True
    for i in range(len(a)-1):
        if abs(a[i+1]-a[i])>1:
            f=False
            break
    if f:
        print("YES")
    else:
        print("NO")
