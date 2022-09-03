a=input()
if int(a)>0:
    print(a)
else:
    if int(a[-2])>int(a[-1]):
        print(int(a[:-2]+a[-1]))
    else:
        print(int(a[:-1]))
