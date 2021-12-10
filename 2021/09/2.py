with open("input.txt") as file: lines = file.read().splitlines()

yMax = len(lines)
xMax = len(lines[0])

visited =set()
dirs = {"R": (1,0), "L": (-1,0), "U": (0,-1), "D": (0,1)}

def nextDirections(dir):
    if(dir=="R"): return ["R", "U", "D"] 
    elif(dir == "L"): return ["L", "U", "D"]
    elif(dir=="D"): return ["L", "D", "R"]
    else: return ["L", "U", "R"]
    
def checkNeighoursInBasin(initialX, initialY, directions, initialSize):
    visited.add((initialX, initialY))
    size=initialSize

    for dir in directions:
        x, y = initialX+dirs[dir][0], initialY + dirs[dir][1]
        nextDirs = nextDirections(dir)

        if (0 <= x < xMax and 0<= y < yMax and lines[y][x]!="9" and (x,y) not in visited):
            size += checkNeighoursInBasin(x, y, nextDirs, initialSize)
                    
    return size+1


def horizontalLow(x, y,num):
    if (x==0):
        return num < lines[y][x+1]
    elif (x==xMax-1):
        return num < lines[y][x-1]
    else:
        return num < lines[y][x+1] and num < lines[y][x-1]

def verticalLow(x, y,num):
    if (y==0):
        return num < lines[y+1][x]
    elif (y==yMax-1):
        return num < lines[y-1][x]
    else:
        return num < lines[y+1][x] and num < lines[y-1][x]

basins =[]
for y in range(yMax):
    for x in range(xMax):
        curr = lines[y][x]
        if horizontalLow(x, y, curr) and verticalLow(x, y, curr):
            basin = checkNeighoursInBasin(x, y, dirs, 0)
            basins.append(basin)
    
print(basins)
mul=1
for i in range(3):
    m = max(basins)
    basins.remove(m)
    mul*=m

print(mul)
