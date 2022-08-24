m,n,a=[int(i) for i in input().split()]
if m%a!=0:
    m=int((m/a)+1)*a
if n%a!=0:
    n=int((n/a)+1)*a
print(m*n//a**2)
