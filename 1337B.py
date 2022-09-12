for i in range(int(input())):
    x,v,l=map(int,input().split())
    while x>20 and v>0 :
        x=(x//2)+10
        v-=1
    x-=(l*10)
    if x>0:
        print("NO")
    else:
        print("YES")
