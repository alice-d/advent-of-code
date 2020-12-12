with open("input") as file:
    lines = file.read().splitlines()

currDir = "E"
x = y = 0
# x -->    y ^

def rotation(array, index, turn, degrees):
    if turn == "L":
        degrees = -degrees
    indexChange = (degrees//90)
    return array[(index+indexChange) % 4]

def changeDir(turn, degrees):
    dirs = ["E", "S", "W", "N"]
    i = dirs.index(currDir)
    return rotation(dirs, i, turn, degrees)

for l in lines:
    action = l[0]
    value = int(l[1:])
    if (action in ["R", "L"]):
        currDir = changeDir(action, value)
    else:
        if (action == "F"):
            action = currDir
        if (action == "N"):
            y += value
        elif (action == "S"):
            y -= value
        elif (action == "E"):
            x += value
        elif (action == "W"):
            x -= value
# print(x,y)
print(abs(x)+abs(y))


# part 2
x = y = 0
wayX = 10
wayY = 1

def rotateWaypoint(action, degrees):
    possibilities = [(wayX, wayY), (wayY, -wayX),
                     (-wayX, -wayY), (-wayY, wayX)]
    i = 0
    return rotation(possibilities, i, action, degrees)

for l in lines:
    action = l[0]
    value = int(l[1:])
    if (action in ["R", "L"]):
        wayX, wayY = rotateWaypoint(action, value)
    elif (action == "N"):
        wayY += value
    elif (action == "S"):
        wayY -= value
    elif (action == "E"):
        wayX += value
    elif (action == "W"):
        wayX -= value
    elif (action == "F"):
        x += value*wayX
        y += value*wayY

#print(wayX, wayY)
# print(x,y)
print(abs(x)+abs(y))
