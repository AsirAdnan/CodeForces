n,k,l,c,d,p,nl,np=list(map(int,input().split()))
drink=(k*l)//nl
lime=c*d
salt=p//np
print(min(drink,lime,salt)//n)
