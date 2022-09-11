for i in range(int(input())):
    input()
    a=input()
    if len(a)==5:
        b=''
        c=''
        for i in a:
            if i==i.upper():
                b+=i
            else:
                c+=i
        
        if b=='T' and 'i' in c and 'm' in c and 'u' in c and 'r' in c:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
