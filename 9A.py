from fractions import Fraction
a=list(map(int,input().split()))
x=Fraction(7-max(a),6)
if x==1:
    print('1/1')
else:
    print(x)
