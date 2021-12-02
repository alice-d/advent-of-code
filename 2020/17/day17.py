from copy import copy, deepcopy
with open("input") as file: lines = file.read().splitlines()

activeCubes=[]
activeHyperCubes=[]
minZ=maxZ=minX=minY=minW=maxW=0
maxX=maxY=len(lines[0])-1
z=y=w=0
for l in lines:
    x=0
    for char in l:
        if (char=="#"):
            activeCubes.append((x,y,z))
            activeHyperCubes.append((x,y,z,w))
        x+=1
    y+=1


def countNeighbors(x,y,z, active):
    n=0
    for zi in range(z-1,z+2):
        for xi in range(x-1,x+2):
            for yi in range(y-1,y+2):
                if (xi==x and yi==y and zi==z):
                    continue
                if ((xi,yi,zi) in active):
                    n+=1
    return n


for i in range(6):
    activeCopy= deepcopy(activeCubes)
    for z in range(minZ-1,maxZ+2):
        for x in range(minX-1,maxX+2):
            for y in range(minY-1,maxY+2):
            
                
                neighors = countNeighbors(x,y,z, activeCopy)
                if (x,y,z) in activeCopy:
                    if (neighors!=2 and neighors!=3):
                        activeCubes.remove((x,y,z))
                else:
                    if (neighors==3):
                        activeCubes.append((x,y,z))
                        maxX=max(maxX,x)
                        maxY=max(maxY,y)
                        maxZ=max(maxZ,z)
                        minX=min(minX,x)
                        minY=min(minY,y)
                        minZ=min(minZ,z)


                
#print(activeCubes)

print(len(activeCubes))
def draw():
    for z in range(minZ, maxZ+1):
        print("z=",z)
        for y in range(minY, maxY+1):
            p=""
            for x in range(minX, maxX+1):
                if (x,y,z) in activeCubes:
                    p+="#"
                else:
                    p+="."
            print(p)
        print()


# part 2
def countNeighborsW(x,y,z, w, active):
    n=0
    for wi in range(w-1,w+2):
        for zi in range(z-1,z+2):
            for xi in range(x-1,x+2):
                for yi in range(y-1,y+2):
                    if (xi==x and yi==y and zi==z and wi==w):
                        continue
                    if ((xi,yi,zi, wi) in active):
                        n+=1
    return n

for i in range(6):
    activeCopy= deepcopy(activeHyperCubes)
    for w in range(minW-1,maxW+2):
        for z in range(minZ-1,maxZ+2):
            for y in range(minY-1,maxY+2):
                for x in range(minX-1,maxX+2):
            
                    neighors = countNeighborsW(x,y,z,w, activeCopy)
                    if (x,y,z,w) in activeCopy:
                        if (neighors!=2 and neighors!=3):
                            activeHyperCubes.remove((x,y,z,w))
                    else:
                        if (neighors==3):
                            activeHyperCubes.append((x,y,z,w))
                            
                            maxX=max(maxX,x)
                            maxY=max(maxY,y)
                            maxZ=max(maxZ,z)
                            minX=min(minX,x)
                            minY=min(minY,y)
                            minZ=min(minZ,z)
                            maxW=max(maxW,w)
                            minW=min(minW,w)

print(len(activeHyperCubes))

