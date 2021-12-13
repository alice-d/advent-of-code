with open("input.txt") as file: lines = file.read().splitlines()

def fold(axis, value, coords):
    newCoords=set()
    if axis=="y":
        for c in coords:
            x,y= c
            if y<value:
                newCoords.add(c)
            else:
                newCoords.add((x, value*2-y))
    if axis=="x":
        for c in coords:
            x,y= c
            if x<value:
                newCoords.add(c)
            else:
                newCoords.add((value*2-x, y))
    return newCoords

def printStuff(coords):
    maxX = max(coords)[0]+1
    maxY = max(coords, key=lambda x:x[1])[1]+1
    map=[["."]*maxX for _ in range(maxY)]

    for c in coords:
        x,y = c
        map[y][x] = "#"
    for line in map:
        print("".join(line))
    print()

coords=set()
currCoords=coords
readingFolds=False

for l in lines:
    if l=="":
        readingFolds=True
    elif not readingFolds:
        x,y = list(map(int,l.split(",")))
        coords.add((x,y))
    else:
        p1, p2 = l.split("=")
        axis =p1[-1]
        value = int(p2)

        coords = fold(axis, value, coords)

printStuff(coords)   



    
