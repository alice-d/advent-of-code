import re
initialV={"Vx":0,"Vy":0,"Vz":0}
planets=[dict(initialV),dict(initialV),dict(initialV),dict(initialV)]

for i in range(4):
    inp=re.sub(r"[ xyz=]","",input()[1:-1])
    coords=list(map(int,inp.split(",")))
    planets[i]["Px"]=coords[0]
    planets[i]["Py"]=coords[1]
    planets[i]["Pz"]=coords[2]

print(planets)

def gravity(coord,planet):
    my=planet[coord]
    vDif=0
    for p in planets:
        if (my<p[coord]):
            vDif+=1
        elif (my>p[coord]):
            vDif-=1
    return vDif

coords=["x","y","z"]

first=[]
for p in planets:
    first.append(dict(p))

def untilRepeat(coord):
    i=0
    while True:
        for p in planets:
            p["V"+coord]+=gravity("P"+coord,p)

        pi=0
        repeat=True
        for p in planets:
            p["P"+coord]+=p["V"+coord]
            if (p["P"+coord]!=first[pi]["P"+coord] or p["V"+coord]!=0):
                repeat=False
            pi+=1
        i+=1
        if (repeat):
            print(i)
            return i

axisCycle={}
for c in coords:
    axisCycle[c]=untilRepeat(c)
print(planets)

#import numpy as np
#print(np.lcm(np.lcm(axisCycle["x"],axisCycle["y"]),axisCycle["z"]))
#the math wasnt working, so i used this
#https://www.calculatorsoup.com/calculators/math/lcm.php
