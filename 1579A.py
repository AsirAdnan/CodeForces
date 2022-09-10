for i in range(int(input())):
    a=input().lower()
    if a.count('a')+a.count('c')==a.count('b'):
        print("YES")
    else:
        print("NO")
