import re
vInicial={"Vx":0,"Vy":0,"Vz":0}
planets=[vInicial,dict(vInicial),dict(vInicial),dict(vInicial)]
coords = ["x","y","z"]
pCoords =["Px","Py","Pz"]
for i in range(4):
    
    inp=input()[1:-1]
    
    inp = re.sub(r'[ =xyz]', '', inp).split(",")
    
    for coord in range(3):
        planets[i][pCoords[coord]]=int(inp[coord])

print(planets)

def gravity(Pcoord,planet):
    
    my=planet[Pcoord]
    vDiff=0

    for p in planets:
        
        if (my>p[Pcoord]):
            vDiff-=1
        elif (my<p[Pcoord]):
            vDiff+=1


    return vDiff

for i in range(1000):
    for p in planets:
        for coord in coords:
            v = gravity("P"+coord,p)
            p["V"+coord]+=v

    for p in planets:
        for coord in coords:      
            p["P"+coord]+=p["V"+coord]

energy=0
for p in planets:
    pot = abs(p["Px"])+abs(p["Py"])+abs(p["Pz"])
    kin = abs(p["Vx"])+abs(p["Vy"])+abs(p["Vz"])
    energy += pot*kin

print()
print(planets)
print(energy)
