for i in range(int(input())):
    input()
    a=list(map(int,input().split()))
    a.sort()
    c=a[-1]-a[0]
    for i in range(len(a)-1):
        if a[i+1]-a[i]<c:
            c=a[i+1]-a[i]
        if c==0:
            break
    print(c)
