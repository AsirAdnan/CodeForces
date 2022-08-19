import itertools
lucky='47'
luckies=[]
for i in range(1,4):
    temp=itertools.product(lucky,repeat=i)
    for j in temp:
        luckies.append(''.join(j))
a=input()
if a in luckies:
    print("YES")
else:
    f=0
    a=int(a)
    for i in luckies:
        if a%int(i)==0:
            f=1
            break
    if f==1:
        print("YES")
    else:
        print("NO")
