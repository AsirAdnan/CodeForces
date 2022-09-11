for i in range(int(input())):
    x=int(input())
    while True:
        x/=2
        if x==1:
            print("NO")
            break
        elif int(x)!=x:
            print("YES")
            break
