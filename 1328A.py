for i in range(int(input())):
    a,b=[int(i) for i in input().split()]
    if a%b==0:
        print(0)
    else:
        print((((a//b)+1)*b)-a)
