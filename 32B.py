c=None
for i in input():
    if i=='.' and c==None:
        print('0',end='')
    elif i=='-' and c==None:
        c='-'
    elif i=='-' and c=='-':
        print('2',end='')
        c=None
    elif i=='.' and c=='-':
        print('1',end='')
        c=None
