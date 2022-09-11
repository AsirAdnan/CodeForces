for _ in range(int(input())):
    input()
    l=''
    s=0
    for i in input():
        if i not in l:
            l+=i
            s+=2
        else:
            s+=1
    print(s)
