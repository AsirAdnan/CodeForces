input()
a=input()
total=0
two=False
one=0
total+=a.count('4')
if a.count('2')%2==0:
    total+=(a.count('2')//2)
else:
    total+=int((a.count('2')/2))
    two=True
if a.count('1')==a.count('3'):
    total+=a.count('1')
elif a.count('1')>=a.count('3'):
    total+=a.count('3')
    one+=(a.count('1')-a.count('3'))
else:
    total+=a.count('1')
    total+=a.count('3')-a.count('1')
if two==True:
    one-=2
    total+=1
if one>0:
    if one%4==0:
        total+=(one//4)
    else:
        total+=int(one/4)+1
print(total)
