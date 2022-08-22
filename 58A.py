a=input()
b='hello'
index=0
for i in a:
    if i==b[index]:
        index+=1
    if index==5:
        print("YES")
        break
if index<5:
    print("NO")
