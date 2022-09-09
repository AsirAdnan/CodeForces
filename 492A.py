c=0
p=int(input())
q=0
i=1
while True:
    c+=1
    x=(c*(c+1))//2
    if p-x<0:
        break
    else:
        q+=x
        p-=x
print(c-1)
