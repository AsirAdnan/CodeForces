tram=0
m=0
for i in range(int(input())):
    x,y=[int(i) for i in input().split()]
    tram-=x
    tram+=y
    if tram>m:
        m=tram
print(m)
