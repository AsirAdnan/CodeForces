for _ in range(int(input())):
    input()
    a=list(map(int,input().split()))
    if sum(a)%2==0:
        if (sum(a)//2)%2==0:
            print("YES")
        else:
            if a.count(1)>=2 and a.count(1)%2==0:
                print("YES")
            else:
                print("NO")
    else:
        print("NO")
