a=input().split("WUB")
t=''
for i in a:
    if len(i)>0:
        if 'WUB' in i:
            t+=i.replace("WUB","")+' '
        else:
            t+=i+' '
print(t[:-1])
