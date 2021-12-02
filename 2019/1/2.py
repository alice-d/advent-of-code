import math

def calc_fuel(total, num):
    fuel = math.floor(num/3)-2
    if fuel<=0:
        #print(total)
        return total
    else:
        return calc_fuel(total+fuel,fuel)

mass=input()
res=0

while mass!='':
    res += calc_fuel(0,int(mass))
    mass=input()

print(res)
