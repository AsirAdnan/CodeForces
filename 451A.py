a,b=[int(i) for i in input().split()]
for i in range(100):
    a-=1
    b-=1
    if a==0 or b==0:
        if i%2==0:
            print("Akshat")
        else:
            print("Malvika")
        break
