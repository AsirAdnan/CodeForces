a=input()
if a==a.upper():
    print(a.lower())
elif a[0]==a[0].lower() and a[1:]==a[1:].upper():
    print(a[0].upper()+a[1:].lower())
else:
    print(a)
