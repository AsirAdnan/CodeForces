for _ in range(int(input())):
    a=int(input())
    if a<=1399:
        print("Division 4")
    elif 1400<=a<=1599:
        print("Division 3")
    elif 1600<=a<=1899:
        print("Division 2")
    else:
        print("Division 1")
