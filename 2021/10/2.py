import statistics
with open("input.txt") as file: lines = file.read().splitlines()

points = {")": 1, "]":2, "}":3, ">":4}
complements = {"(": ")", "[": "]", "{": "}", "<": ">"}
openers =["(","{","[","<"]
scores=[]

for l in lines:
    score=0
    cenas =[]
    corrupted=False
    for elem in l:
        if elem in openers:
            cenas.append(elem)
        else:
            if (elem!=complements[cenas.pop(-1)]):
                corrupted = True
                break
            
    if (not corrupted and len(cenas)!=0):
        end=""
        for _ in range(len(cenas)):
            next = complements[cenas.pop(-1)]
            end+= next
            score*=5
            score+= points[next]
        # print(end)
        # print(score)
        scores.append(score)

print(statistics.median(scores))

