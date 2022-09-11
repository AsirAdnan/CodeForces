for i in range(int(input())):
    x,y,z=list(map(int,input().split()))
    m=abs(x-y)*2
    if x>m or y>m or z>m:
        print(-1)
    else:
        if abs(x-y)+z>m:
            print(z-abs(x-y))
        else:
            print(abs(x-y)+z)
