b=int(input().split()[-1])
a=[int(i) for i in input().split()]
a.sort()
m=min(a)
if b-max(a)>m:
    m=b-max(a)
for i in range(len(a)-1):
    t=abs(a[i]-a[i+1])/2
    if t>m:
        m=t
print('{:.10f}'.format(m))
