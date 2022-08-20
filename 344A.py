c=0
g='a'
for i in range(int(input())):
    x=input()
    if x!=g:
        g=x
        c+=1
print(c)
