for i in range(int(input())):
    a=int(input())
    if (a/2)%2==0:
        print("YES")
        l=[]
        t=2
        for i in range(a//2):
            l.append(t)
            t+=2
        s=sum(l)
        t=1
        for i in range((a//2)-1):
            l.append(t)
            t+=2
        l.append(s-sum(l)+s)
        l=list(map(str,l))
        print(' '.join(l))
    else:
        print("NO")
