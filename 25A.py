input()
a=''
b=input().split()
for i in b:
    a+=str((int(i)%2))
if a.count('0')>a.count('1'):
    print(a.index('1')+1)
else:
    print(a.index('0')+1)
