l=[input().lower(),input().lower()]
x,y=l
l.sort()
if l[0]==l[1]:
    print(0)
elif l[0]==x:
    print(-1)
else:
    print(1)
