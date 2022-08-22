x=int(input().split()[-1])
a=input()
b=''
for _ in range(x):
    tem=None
    for i in range(len(a)-1):
        if i==tem:
            continue
        elif a[i]=="B" and a[i+1]=='G':
            b+='GB'
            tem=i+1
        else:
            b+=a[i]
    if len(b)<len(a):
        b+=a[-1]
    a=b
    b=''
print(a)   
