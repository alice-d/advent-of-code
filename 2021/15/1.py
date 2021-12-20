from collections import Counter
from copy import copy
from os import path
with open("input.txt") as file: lines = file.read().splitlines()

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

while currentPos != (xMax, yMax):
    explore(currentPos)
    
    del pathData[currentPos]
    passedThrough.add(currentPos)
    
    currentPos = pickNext(currentPos)

print(pathData[currentPos])