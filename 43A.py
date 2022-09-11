d=None
x=0
c=int(input())
for i in range(c):
    a=input()
    if d==None:
        d=a
    elif d!=a:
        e=a
    if a==d:
        x+=1
y=c-x
if x>y:
    print(d)
else:
    print(e)
