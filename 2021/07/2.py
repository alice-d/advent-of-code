from collections import Counter
with open("input.txt") as file: lines = file.read().splitlines()

crabs = list(map(int, lines[0].split(",")))
counter = Counter(crabs)

def calcFuelOFMove(fromm, to):
    dist  = abs(fromm-to)
    fuel=0
    for inc in range (1,dist+1):
        fuel += inc
    return fuel

def calcFuel(target):
    fuel=0
    for pos in counter:
        fuel += calcFuelOFMove(target, pos)*counter[pos]
    return fuel

lowestFuel=999999999999
for i in range(max(crabs)):
    posFuel = calcFuel(i)
    if (posFuel < lowestFuel):
        lowestFuel = posFuel
        print("pos: ", i, " ",lowestFuel)
print(lowestFuel)