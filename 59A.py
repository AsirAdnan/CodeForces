l=0
u=0
a=input()
for i in a:
    if i==i.lower():
        l+=1
    else:
        u+=1
if u>l:
    print(a.upper())
else:
    print(a.lower())
