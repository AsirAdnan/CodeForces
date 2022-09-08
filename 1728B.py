for i in range(int(input())):
    l=[]
    x=int(input())
    if x==1:
        print(1)
    elif x==2:
        print("1 2")
    elif x==3:
        print(1,2,3)
    elif x%2==0:
        s=1
        e=x-2
        for i in range((x-1)//2):
            l.append(str(s))
            l.append(str(e))
            s+=1
            e-=1
        l.reverse()
        l.extend([str(x-1),str(x)])
        print(' '.join(l))
    elif x%2!=0:
        s=1
        e=x-2
        y=(x+1)//2
        for i in range((x-2)//2):
            if e==y:
                e-=1
            if s==y:
                s+=1
            l.append(str(e))
            l.append(str(s))
            s+=1
            e-=1
        l.reverse()
        l.extend([str(y),str(x-1),str(x)])
        print(' '.join(l))
