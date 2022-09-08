a=int(input().split()[-1])
b=list(map(int,input().split()))
c=0
for i in b:
    if i+a<=5:
        c+=1
print(c//3)
