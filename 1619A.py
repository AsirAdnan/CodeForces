for _ in range(int(input())):
    a=input()
    if len(a)%2==0:
        if a[:len(a)//2]==a[len(a)//2:]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
