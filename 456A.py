d={}
for i in range(int(input())):
    a,b=map(int,input().split())
    if a in d:
        d[a].append(b)
    else:
        d[a]=[b]
x=list(d.keys())
x.sort()
f=False
for i in range(len(x)-1):
    if max(d[x[i]])>min(d[x[i+1]]):
        f=True
        break
if f:
    print("Happy Alex")
else:
    print("Poor Alex")
