for i in range(int(input())):
    a=int(input())
    j=1
    c=0
    while True:
        if j%3!=0 and str(j)[-1]!='3':
            c+=1
            if c==a:
                print(j)
                break
            else:
                j+=1
        else:
            j+=1
