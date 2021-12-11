with open("input.txt") as file: lines = file.read().splitlines()

xMax = len(lines[0])
yMax= len(lines)

for y in range(yMax):
    lineInList = []
    lineInList[:0] = lines[y]
    lines[y]= lineInList

flashes =0
dirs = [(0,1),(1,1),(1,0),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]

def flash(x,y):
    for d in dirs:
        vizinhoX,vizinhoY = x+d[0], y+d[1]
        if (vizinhoX<0 or vizinhoX>=xMax or vizinhoY<0 or vizinhoY>=yMax): continue
        energyUp(vizinhoX,vizinhoY)

def energyUp(x,y):
    global lines
    global flashes
    
    numS = lines[y][x]
    if numS=="F":
        return
    num =int(numS)
    if (num==9):
        flashes+=1
        lines[y][x] = "F"
        flash(x,y)
    else:
        lines[y][x] = str(num+1)

def cleanUpFlashed():
    for y in range(yMax):
        lines[y][:] = [n if n != 'F' else "0" for n in lines[y]]

def printCenas():
    for l in lines:
        print("".join(l))

for step in range(1000):
    prevFlashes=flashes
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            energyUp(x,y)
    cleanUpFlashed()
    
    flashesDiff=flashes-prevFlashes
    if (flashesDiff==100):
        print("All flashed at step ", step+1)
        break
    # print(step+1)
printCenas()
    
print(flashes)

