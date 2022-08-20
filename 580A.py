input()
a=[int(i) for i in input().split()]
b=[]
c=1
for i in range(len(a)-1):
    if a[i+1]>=a[i]:
        c+=1
    else:
        b.append(c)
        c=1
b.append(c)
print(max(b))
