with open("input.txt") as file: lines = file.read().splitlines()

points = {")": 3, "]":57, "}":1197, ">":25137}
complements = {")": "(", "]": "[", "}": "{", ">": "<"}
openers =["(","{","[","<"]
score=0
for l in lines:
    cenas =[]
    for elem in l:
        if elem in openers:
            cenas.append(elem)
        else:
            if (complements[elem]!=cenas.pop(-1)):
                #print(elem)
                score += points[elem]
                break

print(score)

