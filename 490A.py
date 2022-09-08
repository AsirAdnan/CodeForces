input()
a=input().split()
l=[]
one=[]
two=[]
three=[]
for i in range(len(a)):
    if a[i]=='1':
        one.append(i+1)
    elif a[i]=='2':
        two.append(i+1)
    else:
        three.append(i+1)
if len(one)==min(len(one),len(two),len(three)):
    for i in range(len(one)):
        l.append([str(one[i]),str(two[i]),str(three[i])])
elif len(two)==min(len(one),len(two),len(three)):
    for i in range(len(two)):
        l.append([str(one[i]),str(two[i]),str(three[i])])
else:
    for i in range(len(three)):
        l.append([str(one[i]),str(two[i]),str(three[i])])
print(len(l))
for i in l:
    print(' '.join(i))
