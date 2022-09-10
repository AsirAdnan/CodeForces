for i in range(int(input())):
    input()
    e=0
    o=0
    a=list(map(int,input().split()))
    for i in a:
        if i%2==0:
            e+=1
        else:
            o+=1
    if o%2!=0:
        print("YES")
    elif o>0 and o%2==0 and e>0:
        print("YES")
    else:
        print("NO")
