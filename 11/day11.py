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

def searchNear(mapa, i, j, isCount):
    count=0
    if (i>0):
        if (mapa[i-1][j]=="#"): 
            if isCount:count+=1
            else: return False
        if (j>0 and mapa[i-1][j-1]=="#"):
            if isCount:count+=1
            else: return False
        if (j<length-1 and mapa[i-1][j+1]=="#"):
            if isCount:count+=1
            else: return False
    if (i<height-1):
        if (mapa[i+1][j]=="#"): 
            if isCount:count+=1
            else:return False
        if (j>0 and mapa[i+1][j-1]=="#"):
            if isCount:count+=1
            else: return False
        if (j<length-1 and mapa[i+1][j+1]=="#"):
            if isCount:count+=1
            else: return False
    if (j>0):
        if (mapa[i][j-1]=="#"): 
            if isCount:count+=1
            else:return False
    if (j<length-1):
        if (mapa[i][j+1]=="#"): 
            if isCount:count+=1
            else:return False

    if isCount:return count>=4
    else: return True

def applyRules(oldMap):
    newMap=deepcopy(oldMap)
    for i in range(height):
        for j in range(length):
            seat = oldMap[i][j]
            if (seat=="L" and searchNear(oldMap,i,j, False)):
                newMap[i][j]="#"
            elif (seat == "#" and searchNear(oldMap,i,j, True)):
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
    #printMap(newMap)
    if (newMap==oldMap):
        print(countOccupied(newMap))
        break
    oldMap=deepcopy(newMap)

down = lambda i : range(i+1,height)
up = lambda i : range(i-1,-1,-1)
left = lambda j: range(j-1, -1,-1)
right = lambda j: range(j+1,length)
 
#part 2
def searchLinesTudo(mapa, i, j, isCount):
    vertical= [up(i),down(i)]
    horizontal=[left(j),right(j)]
    occupied=0
    for d in vertical:
        for y in d:
            if (mapa[y][j]=="#"):
                if (isCount): occupied+=1
                else: return False
                break
            elif (mapa[y][j]=="L"): break
        for subDir in horizontal:
            for y,x in zip(d, subDir):
                if (mapa[y][x]=="#"):
                    if (isCount): occupied+=1
                    else: return False
                    break
                elif (mapa[y][x]=="L"): break
    for d in horizontal:
        for x in d:
            if (mapa[i][x]=="#"):
                if (isCount): occupied+=1
                else: return False
                break
            elif (mapa[i][x]=="L"): break
    if (isCount): return occupied>=5
    else: return True

def applyRules2(oldMap):
    newMap=deepcopy(oldMap)
    for i in range(height):
        for j in range(length):
            seat = oldMap[i][j]
            if (seat=="L" and searchLinesTudo(oldMap,i,j, False)):
                newMap[i][j]="#"
            elif (seat == "#" and searchLinesTudo(oldMap,i,j, True)):
                newMap[i][j]="L"       
    return (newMap)

while True:
    newMap = applyRules2(lines)
    #printMap(newMap)
    if (newMap==lines):
        print(countOccupied(newMap))
        break
    lines=deepcopy(newMap)
