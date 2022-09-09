for _ in range(int(input())):
    a=[int(i) for i in input().split()]
    n=a.pop()
    x=max(a)
    for i in a:
        n-=(x-i)
    if n%3==0 and n>=0:
        print("YES")
    else:
        print("NO")
