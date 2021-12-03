with open("input.txt") as file: lines = file.read().splitlines()

numOfBits = len(lines[0])
numOfNums = len(lines)
bitsCount = {"0": 0, "1":0}
gammaBin=""
episBin=""

for i in range(numOfBits):
    for num in range(numOfNums):
        bitsCount[lines[num][i]] +=1
    if bitsCount["0"] > bitsCount["1"]:
        gammaBin +="0"
        episBin += "1"
    else:
        gammaBin +="1"
        episBin += "0"
    bitsCount = {"0": 0, "1":0}

gamma = int(gammaBin, 2)
eps = int(episBin, 2)
print(gamma*eps)