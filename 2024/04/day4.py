import re
with open("input.txt") as file: lines = file.read().splitlines()

xmas = "XMAS"
samx = "SAMX"
xLen = len(lines[0])
yLen = len(lines)
count = 0
for line in lines:
    foundXMAS = line.count(xmas)
    if (foundXMAS >0):
        count += foundXMAS
    foundSAMX = line.count(samx)
    if (foundSAMX > 0):
        count += foundSAMX


def findXmasInIncrements(nextX,nextY, xInc, YInc, xmasIndex):
    if (lines[nextY][nextX] == xmas[xmasIndex]):
        if (xmasIndex==3):
            return 1
        xmasIndex +=1
        nextX +=xInc
        nextY +=YInc
        if (0 <= nextX < xLen and 0<= nextY < yLen):
            return findXmasInIncrements(nextX,nextY, xInc, YInc, xmasIndex)
    return 0

def search(x,y, xmasIndex):
    found = 0
    if (y  < yLen - 1):#can go Down
        nextY = y+1
        found += findXmasInIncrements(x, nextY, 0, 1, xmasIndex)
        if (x < xLen - 1): # can go right
            nextX = x+1
            found += findXmasInIncrements(nextX, nextY, 1, 1, xmasIndex)
        if (x > 0): # can go left
            nextX = x-1
            found += findXmasInIncrements(nextX, nextY, -1, 1, xmasIndex)
    if (y>0):#can go up 
        nextY = y-1
        found += findXmasInIncrements(x, nextY, 0, -1, xmasIndex)
        if (x < xLen - 1): # can go right
            nextX = x+1
            found += findXmasInIncrements(nextX, nextY, 1, -1, xmasIndex)
        if (x > 0): # can go left
            nextX = x-1
            found += findXmasInIncrements(nextX, nextY, -1, -1, xmasIndex)
    return found
            
def findFromXOnwards(currLine, cutSize = 0):
    found = 0
    if(currLine.find("X")!=-1):
        lineIndex = currLine.index("X")
        xIndex = lineIndex + cutSize
        found += search(xIndex, y, 1)
        if (xIndex < xLen -1):
            subLine = currLine[lineIndex+1:]
            found += findFromXOnwards(subLine, xIndex+1)
    return found

for y in range(yLen):
    line = lines[y]
    count += findFromXOnwards(line)   

print("PART 1: ", count)

countMas=0
def hasMAS(x,y):
    dr = lines[y+1][x+1]
    ul = lines[y-1][x-1]
    dl = lines[y+1][x-1]
    ur = lines[y-1][x+1]
    return (((dr == "M" and ul == "S") or (dr == "S" and ul == "M"))
        and ((dl == "M" and ur == "S") or (dl == "S" and ur == "M")))


def findFromAOnwards(currLine, cutSize = 0):
    found = 0
    if(currLine.find("A")!=-1):
        lineIndex = currLine.index("A")
        xIndex = lineIndex + cutSize
        if (hasMAS(xIndex, y)):
            found +=1
        if (xIndex < xLen -1): # find next occurrence of A
            subLine = currLine[lineIndex+1:]
            found += findFromAOnwards(subLine, xIndex+1)
    return found

for y in range(1, yLen-1):
    line = lines[y]
    countMas += findFromAOnwards(line[1:-1], 1)   

print("PART 2: ", countMas)