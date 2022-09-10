for _ in range(int(input())):
    input()
    a=input().split()
    l=[]
    for i in range(len(a)//2):
        l.extend([a[i],a[len(a)-1-i]])
    if len(a)%2!=0:
        l.append(a[int(len(a)/2)])
    print(' '.join(l))
