f=True
for i in range(int(input().split()[0])):
    t=input().split()
    if f:
        if 'C' in t or 'M' in t or 'Y' in t:
            f=False
if f:
    print("#Black&White")
else:
    print("#Color")
