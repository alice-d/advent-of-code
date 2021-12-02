import math

mass=input()
res=0
while mass!='':
    
    res+=math.floor(int(mass)/3)-2
    mass=input()
print(res)
