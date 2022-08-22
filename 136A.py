x=[0]*int(input())
y=[int(i) for i in input().split()]
for i in range(len(y)):
    x[y[i]-1]=str(i+1)
print(' '.join(x))
