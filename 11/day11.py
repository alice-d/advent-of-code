from copy import deepcopy
with open("input") as file:lines = file.read().splitlines()

length=len(lines[0])
height=len(lines)

for i in range(height):
    lines[i]=list(lines[i])

def printMap(mapa):
    for m in mapa:
        print("".join(m))
    print()

def sozinho(mapa, i, j):
    if (i>0):
        if (mapa[i-1][j]=="#"): return False
        if (j>0):
            if (mapa[i-1][j-1]=="#"):return False
        if (j<length-1):
            if (mapa[i-1][j+1]=="#"):return False
    if (i<height-1):
        if (mapa[i+1][j]=="#"): return False
        if (j>0):
            if (mapa[i+1][j-1]=="#"):return False
        if (j<length-1):
            if (mapa[i+1][j+1]=="#"):return False
    if (j>0):
        if (mapa[i][j-1]=="#"): return False
    if (j<length-1):
        if (mapa[i][j+1]=="#"): return False
    return True

def peopleAroud(mapa,i,j):
    vizinhos=0
    if (i>0):
        if (mapa[i-1][j]=="#"): vizinhos+=1
        if (j>0):
            if (mapa[i-1][j-1]=="#"): vizinhos+=1
        if (j<length-1):
            if (mapa[i-1][j+1]=="#"): vizinhos+=1
    if (i<height-1):
        if (mapa[i+1][j]=="#"): vizinhos+=1
        if (j>0):
            if (mapa[i+1][j-1]=="#"): vizinhos+=1
        if (j<length-1):
            if (mapa[i+1][j+1]=="#"): vizinhos+=1
    if (j>0):
        if (mapa[i][j-1]=="#"): vizinhos+=1
    if (j<length-1):
        if (mapa[i][j+1]=="#"): vizinhos+=1
    return vizinhos>=4

def applyRules(oldMap):
    newMap=deepcopy(oldMap)
    for i in range(height):
        for j in range(length):
            seat = oldMap[i][j]
            if (seat=="L" and sozinho(oldMap,i,j)):
                newMap[i][j]="#"
            elif (seat == "#" and peopleAroud(oldMap,i,j)):
                newMap[i][j]="L"
    
    return (newMap)

def countOccupied(mapa):
    occupied=0
    for m in mapa:
        occupied+=m.count("#")
    return occupied

#part 1
oldMap=deepcopy(lines)
while True:
    newMap = applyRules(oldMap)
    if (newMap==oldMap):
        print(countOccupied(newMap))
        break
    oldMap=deepcopy(newMap)

#part 2
def noVisiblePeople(mapa, i, j):
    if (i>0):
        for y in range(i-1,-1,-1):
            if (mapa[y][j]=="#"):return False
            elif (mapa[y][j]=="L"): break
        if (j>0):
            for y,x in zip(range(i-1, -1,-1), range(j-1, -1,-1)):
                if (mapa[y][x]=="#"):return False
                elif (mapa[y][x]=="L"): break
        if (j<length-1):
            for y,x in zip(range(i-1, -1,-1), range(j+1,length)):
                if (mapa[y][x]=="#"):return False
                elif (mapa[y][x]=="L"): break
    if (i<height-1):
        for y in range(i+1,height):
            if (mapa[y][j]=="#"):return False
            elif (mapa[y][j]=="L"): break
        if (j>0):
            for y,x in zip(range(i+1,height), range(j-1, -1,-1)):
                if (mapa[y][x]=="#"):return False
                elif (mapa[y][x]=="L"): break
        if (j<length-1):
            for y,x in zip(range(i+1, height), range(j+1, length)):
                if (mapa[y][x]=="#"):return False
                elif (mapa[y][x]=="L"):break
    if (j>0):
        for x in range(j-1,-1,-1):
            if (mapa[i][x]=="#"):return False
            elif (mapa[i][x]=="L"): break
    if (j<length-1):
        for x in range(j+1,length):
            if (mapa[i][x]=="#"):return False
            elif (mapa[i][x]=="L"): break
    return True

def peopleVisible(mapa, i, j):
    occupied=0
    if (i>0):
        for y in range(i-1,-1,-1):
            if (mapa[y][j]=="#"):
                occupied+=1
                break
            elif (mapa[y][j]=="L"): break
        
        if (j>0):
            for y,x in zip(range(i-1, -1,-1), range(j-1, -1,-1)):
                if (mapa[y][x]=="#"):
                    occupied+=1
                    break
                elif (mapa[y][x]=="L"): break

        if (j<length-1):
            for y,x in zip(range(i-1, -1,-1), range(j+1,length)):
                if (mapa[y][x]=="#"):
                    occupied+=1
                    break
                elif (mapa[y][x]=="L"): break

    if (i<height-1):
        for y in range(i+1,height):
            if (mapa[y][j]=="#"):
                occupied+=1
                break
            elif (mapa[y][j]=="L"): break
        if (j>0):
            for y,x in zip(range(i+1,height), range(j-1, -1,-1)):
                if (mapa[y][x]=="#"):
                    occupied+=1
                    break
                elif (mapa[y][x]=="L"): break
        if (j<length-1):
            for y,x in zip(range(i+1, height), range(j+1, length)):
                if (mapa[y][x]=="#"):
                    occupied+=1
                    break
                elif (mapa[y][x]=="L"):break
    if (j>0):
        for x in range(j-1,-1,-1):
            if (mapa[i][x]=="#"):
                occupied+=1
                break
            elif (mapa[i][x]=="L"): break
    if (j<length-1):
        for x in range(j+1,length):
            if (mapa[i][x]=="#"):
                occupied+=1
                break
            elif (mapa[i][x]=="L"): break
    return occupied>=5

def applyRules2(oldMap):
    newMap=deepcopy(oldMap)
    for i in range(height):
        for j in range(length):
            seat = oldMap[i][j]
            if (seat=="L" and noVisiblePeople(oldMap,i,j)):
                newMap[i][j]="#"
            elif (seat == "#" and peopleVisible(oldMap,i,j)):
                newMap[i][j]="L"       
    return (newMap)

while True:
    newMap = applyRules2(lines)
    #printMap(newMap)

    if (newMap==lines):
        print(countOccupied(newMap))
        break
    lines=deepcopy(newMap)

