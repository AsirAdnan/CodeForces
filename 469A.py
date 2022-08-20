n=int(input())
a=input().split()
a.pop(0)
a.extend(input().split()[1:])
f=1
for i in range(1,n+1):
    if str(i) not in a:
        f=0
        break
if f==1:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
