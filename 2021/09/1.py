with open("input.txt") as file: lines = file.read().splitlines()

yMax = len(lines)
xMax = len(lines[0])
sum = 0

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

for y in range(yMax):
    for x in range(xMax):
        curr = lines[y][x]
        if horizontalLow(x, y, curr) and verticalLow(x, y, curr):
            sum += int(curr)+1
    
print(sum)