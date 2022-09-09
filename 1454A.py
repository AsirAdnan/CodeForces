for _ in range(int(input())):
    a=int(input())
    l=[str(a)]
    for i in range(1,a):
        l.append(str(i))
    print(' '.join(l))
