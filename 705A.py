a=['I love that ',"I hate that "]
b=['I love it','I hate it']
f=1
empty=''
for i in range(int(input())-1):
    empty+=a[f]
    if f==1:
        f=0
    else:
        f=1
print(empty+b[f])
