for i in range(int(input())):
    input()
    a=input().split()
    g=None
    x=0
    for i in range(len(a)):
        if a[0]==a[i]:
            x+=1
        else:
            g=i
    if x==1:
        print(1)
    else:
        print(g+1)
