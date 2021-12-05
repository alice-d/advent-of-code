with open("input.txt") as file: lines = file.read().splitlines()

sizeOfMap=1000
diagram=[[0]*sizeOfMap for _ in range(sizeOfMap)]
def printMap():
    for l in diagram:
        print(l)

above2=0
for l in lines:
    # print(l)
    fromm, to = l.split(" -> ")
    x1, y1 = list(map(int,fromm.split(",")))
    x2, y2 = list(map(int,to.split(",")))

    if x1!=x2 and y1!=y2:
        continue
    if x1 == x2:
        if y1>y2:
            y1, y2 = y2, y1
        for y in range(y1,y2+1):
            diagram[y][x1] +=1
            if diagram[y][x1]==2:
                above2+=1
    elif y1 == y2:
        if x1>x2:
            x1, x2 = x2, x1
        for x in range(x1,x2+1):
            diagram[y1][x] +=1
            if diagram[y1][x]==2:
                above2+=1

# printMap()
print(above2)     