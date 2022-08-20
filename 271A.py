a=int(input())
for i in range(a+1,100000):
    tem=''
    for j in str(i):
        if j not in tem:
            tem+=j
    if len(tem)==4:
        break
print(tem)
