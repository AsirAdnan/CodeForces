a=input()
b=input().split()
f=False
for i in b:
    if i[0]==a[0] or i[1]==a[1]:
        f=True
        break
if f:
    print("YES")
else:
    print("NO")
