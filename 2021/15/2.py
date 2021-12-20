from collections import Counter
from copy import copy
from os import path
with open("input.txt") as file: lines = file.read().splitlines()

yMax= len(lines)-1
xMax= len(lines[0])-1
def incNumsInString(string, inc):
    ret=""
    for c in string:
        num =int(c)
        if num+inc>9:
            ret+=str((num+inc)%9)
        else:
            ret+=str(num+inc)
    return ret

for i in range(len(lines)):
    l = lines[i]
    lines[i] = l + incNumsInString(l, 1) + incNumsInString(l, 2) + incNumsInString(l, 3) + incNumsInString(l, 4)

added=0
for i in range (1,5):
    for y in range(yMax+1):
        lines.append( incNumsInString(lines[y], i))
        added+=1

yMax= len(lines)-1
xMax= len(lines[0])-1

pathData={(0,0): {"cost": 0, "dist": yMax+xMax}}
passedThrough = set()
currentPos=(0,0)
dirs={(1,0),(0,1),(-1,0),(0,-1)}

def explore(coord):
    cost = pathData[coord]["cost"]
    for d in dirs:
        x,y = coord
        x += d[0]
        y += d[1]

        if  0 <= x <= xMax and 0<= y <= yMax:
            nextCoord = (x,y)
            nextCost = cost + int(lines[y][x])
            nextDist=yMax-y+xMax-x
            if nextCoord not in passedThrough and (nextCoord not in pathData  or pathData[nextCoord]['cost'] > nextCost):
                pathData[nextCoord] = {"cost": nextCost, "dist": nextDist}

def pickNext(coord):
    leastCostDistCoord=None 

    for coord in pathData:
        if leastCostDistCoord==None or pathData[coord]['cost'] + pathData[coord]['dist'] < leastCostDist:
            leastCostDistCoord=coord
            leastCostDist=pathData[coord]['cost'] + pathData[coord]['dist']

    return leastCostDistCoord


while True:                 
    if (currentPos == (xMax, yMax)):
        print(pathData[currentPos])
        break

    ## check directions and calculate costs
    explore(currentPos)
    
    ##remove current from pathsCost
    del pathData[currentPos]
    passedThrough.add(currentPos)
    
    ##pick best next position
    currentPos = pickNext(currentPos)