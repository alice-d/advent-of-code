from copy import copy
with open("input.txt") as file: lines = file.read().splitlines()

def countBits(numList, i):
    bitsCount = {"0": 0, "1":0}
    for num in range(len(numList)):
        bitsCount[numList[num][i]] +=1
    return bitsCount

gammaBits=[]
numOfBits = len(lines[0])

bitsCount = {"0": 0, "1":0}
O2binary =""
CO2binary =""
O2Nums=copy(lines)
CO2Nums=copy(lines)

for i in range(numOfBits):
    bitsCount = countBits(O2Nums, i)

    if bitsCount["0"] > bitsCount["1"]:
        O2binary +="0"
    else:
        O2binary +="1"
    O2Nums = list(filter(lambda a: a.startswith(O2binary),O2Nums))
    
    bitsCount = countBits(CO2Nums, i)
        
    if bitsCount["0"]==0:
        CO2binary +="1"
    elif  bitsCount["1"]==0:
        CO2binary +="0"
    elif bitsCount["0"] > bitsCount["1"]:
        CO2binary +="1"
    else:
        CO2binary +="0"
    CO2Nums = list(filter(lambda a: a.startswith(CO2binary),CO2Nums))

O2 = int(O2binary,2)
CO2 = int(CO2binary,2)
print("O2: ",O2binary, ", ", O2)
print("CO2: ",CO2binary, ", ", CO2)
print(O2*CO2)