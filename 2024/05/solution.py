import re
with open("input.txt") as file: lines = file.read().splitlines()

countValids=0
countCorrected =0
order ={}
endPart =[]
for i in range(len(lines)):
    line = lines[i]
    if (line==""):
        endPart = lines[i+1:]
        break
    before, after = line.split("|")
    if before in order:
        order[before]["<"].append(after)
    else:
        order[before] = {"<": [after], ">": []}
    
    if after in order:
        order[after][">"].append(before)
    else:
        order[after] = {">": [before], "<": []}

def valid(sequence, i):
    num = sequence[i]
    before = sequence[:i]
    after = sequence[i+1:]
    for b in before:
        if (b  in order[num]["<"]):
            return False
    for a in after:
        if (a  in order[num][">"]):
            return False
    return True

def findInvalid(sequence):
    seqSize = len(sequence)
    for i in range(seqSize):
        if (not valid(sequence, i)):
            return i

def reorder(sequence, i):
    num = sequence[i]
    before = sequence[:i]
    after = sequence[i+1:]

    for j in range(len(after)):
        if (after[j]  in order[num][">"]):
            ordered = before + [after[j]] + sequence[i+1:i+j+1]  + [num] + after[j+1:]
            newI = findInvalid(ordered)
            if newI != None: 
                return reorder(ordered, newI)
            return ordered

for update in endPart:
    sequence = update.split(",")
    seqSize = len(sequence)
    for i in range(seqSize):
        
        if (not valid(sequence, i)):
            reordered = reorder(sequence, i)
            middle  = int(reordered[seqSize//2])
            countCorrected+=middle
            findInvalid(reordered)
            break

        if (i == seqSize-1):
            middle  = int(sequence[seqSize//2])
            countValids+=middle

print("PART 1: ", countValids)
print("PART 2: ", countCorrected)
