a,b=list(map(int,input().split()))
c=1
p=a
while True:
    if p%10==0 or p%10==b:
        break
    c+=1
    p=a*c
print(c)
