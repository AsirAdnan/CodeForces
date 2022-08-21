a=int(input())
if a<26:
    input()
    print("NO")
else:
    b=input().lower()
    f=True
    for i in range(97,123):
        if chr(i) not in b:
            f=False
            print("NO")
            break
    if f==True:
        print("YES")
