input()
a=[int(i) for i in input().split()]
b=[a[0]]
c=0
if len(a)>1:
    for i in range(1,len(a)):
        if a[i]>max(b) or a[i]<min(b):
            c+=1
        b.append(a[i])
print(c)
