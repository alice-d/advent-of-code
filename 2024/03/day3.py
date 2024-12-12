import re
with open("input.txt") as file: lines = file.read().splitlines()

muls =[]
for line in lines:
    lineMuls = re.findall("mul\((\d{1,3}),(\d{1,3})\)", line)
    muls  += lineMuls

soma=0
for mul in muls:
    soma += int(mul[0]) * int(mul[1])
print("PART 1: ",soma)


muls =[]
for line in lines:
    lineMuls = re.findall("(?:mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))", line)
    muls  += lineMuls

soma=0
enabled = True
for mul in muls:
    if (mul[2]=="do()"):
        enabled = True
        continue
    if (mul[3] == "don't()"):
        enabled = False
        continue

    if (enabled):
        soma += int(mul[0]) * int(mul[1])
print("PART 2: ", soma)