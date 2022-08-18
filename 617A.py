a=[5,4,3,2,1]
x=int(input())
i=0
s=0
while s<x:
    for j in a:
        if s+j<=x:
            s+=j
            break
    i+=1
print(i)
