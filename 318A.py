x,y=[int(i) for i in input().split()]
if x%2==0:
    if y<=(x//2):
        print((y*2)-1)
    else:
        print((y*2)-x)
else:
    if y<=((x+1)//2):
        print((y*2)-1)
    else:
        print((y*2)-x-1)
