x=0
for i in range(int(input())):
    a=input().lower()
    if 'x++' in a or '++x' in a:
        x+=1
    elif 'x--' in a or '--x' in a:
        x-=1
print(x)
