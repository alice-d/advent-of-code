with open("input") as file:
    lines = list(map(int, file.read().splitlines()))

preSize = 25

def isValid(num, prev):
    prev.sort()
    i = 0
    j = preSize - 1
    while i < j:
        soma = prev[i] + prev[j]
        # print("sum: ",prev[i],prev[j], " -> ",soma)
        if soma == num:
            return True
        elif soma > num:
            j -= 1
        elif soma < num:
            i += 1
    return False

def numberWithoutSumOfPrev():
    for i in range(preSize, len(lines)):
        prev = lines[i - preSize : i]
        # print(prev)
        # print(lines[i])
        if not (isValid(lines[i], prev)):
            return lines[i]

# part 1
thatNumber = numberWithoutSumOfPrev()
print(thatNumber, " is not valid.")

# part 2
currArray = [lines[0]]
i = 0
j = 1
while True:
    soma = sum(currArray)
    if soma == thatNumber:
        # print(currArray)
        currArray.sort()
        # print(currArray[0],currArray[-1])
        print("sum: ", currArray[0] + currArray[-1])
        break
    elif soma < thatNumber:
        j += 1
    elif soma > thatNumber:
        i += 1
    currArray = lines[i:j]