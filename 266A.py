input()
a=input()
start=a[0]
count=0
for i in range(1,len(a)):
    if a[i]==start:
        count+=1
    else:
        start=a[i]
print(count)
