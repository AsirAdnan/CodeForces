for _ in range(int(input())):
    a=input()
    s=0
    p=0
    for i in range(6):
        if i<=2:
            s+=int(a[i])
        else:
            p+=int(a[i])
    if s==p:
        print("YES")
    else:
        print("NO")
