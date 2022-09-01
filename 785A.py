c=0
for _ in range(int(input())):
    x=input()
    if x=='Icosahedron':
        c+=20
    elif x=='Dodecahedron':
        c+=12
    elif x=='Cube':
        c+=6
    elif x=='Octahedron':
        c+=8
    else:
        c+=4
print(c)
