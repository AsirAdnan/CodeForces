v='aeiouy'
a=input().lower()
for i in v:
    if i in a:
        a=a.replace(i,'')
for i in a:
    print(f'.{i}',end='')
