for i in range(int(input())):
    x=int(input())
    s=(int(str(x)[0])-1)*10
    for i in range(1,len(str(x))+1):
        s+=i
    print(s)
