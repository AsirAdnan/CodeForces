a='qwertyuiopasdfghjkl;zxcvbnm,./'
b=''
if input()=='R':
    for i in input():
        b+=a[a.index(i)-1]
else:
    for i in input():
        b+=a[a.index(i)+1]
print(b)
