c=0
for i in range(int(input())):
    x,y=[int(i) for i in input().split()]
    if y-x>=2:
        c+=1
print(c)
