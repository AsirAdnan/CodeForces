for i in range(int(input())):
    a=input()
    c=2
    b=''
    for i in range(len(a)):
        if i==c:
            c+=2
        else:
            b+=a[i]
    print(b)
