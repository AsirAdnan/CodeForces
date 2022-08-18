input()
l=[int(i) for i in input().split()]
l.sort(reverse=True)
s=0
i=0
while s<=sum(l):
    s+=l.pop(0)
    i+=1
print(i)
