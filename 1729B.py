for i in range(int(input())):
    input()
    b=input()[::-1]
    x='abcdefghijklmnopqrstuvwxyz'
    z=''
    i=0
    while i<(len(b)):
        if b[i]=='0':
            c=int(b[i+2]+b[i+1])
            i+=3
        else:
            c=int(b[i])
            i+=1
        z+=x[c-1]
    print(z[::-1])
            
