for i in range(int(input())):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    while c<k:
        if max(b)-min(a)>0:
            a[a.index(min(a))],b[b.index(max(b))]=b[b.index(max(b))],a[a.index(min(a))]
            c+=1
        else:
            break
    print(sum(a))
