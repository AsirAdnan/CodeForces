import math
for i in range(int(input())):
    a=int(input())/3
    if a-int(a)<.5:
        print(math.ceil(a),int(a))
    else:
        print(int(a),math.ceil(a))
