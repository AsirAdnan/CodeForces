input()
a=[int(i) for i in input().split()]
c=0
p=0
for i in a:
    if i<0:
        if p==0:
            c+=1
        else:
            p-=1
    else:
        p+=i
print(c)
