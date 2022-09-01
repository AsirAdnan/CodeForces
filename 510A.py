n,m=[int(i) for i in input().split()]
f=True
for i in range(n):
    if i%2==0:
        print("#"*m)
    else:
        if f:
            print('.'*(m-1)+'#')
            f=False
        else:
            print('#'+'.'*(m-1))
            f=True
