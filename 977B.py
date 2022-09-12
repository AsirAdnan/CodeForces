input()
d={}
a=input()
for i in range(len(a)-1):
    s=a[i]+a[i+1]
    if s in d:
        d[s]+=1
    else:
        d[s]=1
m=0
for i,j in d.items():
    if j>m:
        m=j
        s=i
print(s)
