a=[]
for i in range(int(input())):
    a.append(input().split())
c=0
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            if a[i][0]==a[j][1]:
                c+=1
print(c)
