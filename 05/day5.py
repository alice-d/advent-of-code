def calc(min,max):
    return ((max-min)+1)//2 + min

def calculate_seat(passe):
    rowMin=colMin=0
    rowMax=127
    colMax=7
    for p in passe:
        if (p=="B"):
            rowMin = calc(rowMin,rowMax)
        elif (p=="F"):
            rowMax = calc(rowMin,rowMax) -1
        elif (p=="R"):
            colMin = calc(colMin,colMax)
        else:
            colMax = calc(colMin,colMax) -1
    #print(rowMin, rowMax)
    #print(colMin, colMax)
    id=rowMin*8+colMin
    #print(id)
    return id

with open("input") as file: lines = file.read().splitlines()
max=-1
#part 1
for l in lines:
    id=calculate_seat(l)
    if(id>max):max=id

print(max)

#part 2
ids = []
for l in lines:
    id=calculate_seat(l)
    ids.append(id)
    ids.sort()

for i in range(80, max+1):
    if (i not in ids):
        print(i)