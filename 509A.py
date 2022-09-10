a=int(input())
l=[[1]*a]
for i in range(a-1):
    t=[]
    for j in range(a):
        if j==0:
            t.append(l[i][j])
        else:
            t.append(l[i][j]+t[j-1])
    l.append(t)
print(l[-1][-1])
