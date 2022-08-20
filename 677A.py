y=int(input().split()[-1])
x=[int(i) for i in input().split()]
w=0
for i in x:
    if i>y:
        w+=2
    else:
        w+=1
print(w)
