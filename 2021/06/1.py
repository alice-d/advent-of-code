with open("input.txt") as file: lines = file.read().splitlines()

ages = list(map(int, lines[0].split(",")))

for day in range(80):
    newFishes=0
    for i in range(len(ages)):
        if (ages[i]==0):
            newFishes+=1
            ages[i]=6
        else:
            ages[i] -= 1
    ages = ages + [8]*newFishes
    #print("Day ", day+1, " : ", ages)
print(len(ages))