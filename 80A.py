a,b=list(map(int,input().split()))
a+=1
while a<=b:
    f=True
    for i in range(2,a):
        if a%i==0:
            f=False
            break
    if f:
        if a==b:
            print("YES")
        else:
            print("NO")
        break
    a+=1
    if a>b:
        print("NO")
