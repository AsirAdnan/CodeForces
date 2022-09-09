a,b,c,d=list(map(int,input().split()))
s=0
for i in input():
    if i=='1':
        s+=a
    elif i=='2':
        s+=b
    elif i=='3':
        s+=c
    else:
        s+=d
print(s)
