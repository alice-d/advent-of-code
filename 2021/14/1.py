from collections import Counter
with open("input.txt") as file: lines = file.read().splitlines()
polymer = lines[0]

pairs ={}
for l in lines[2:]:
    left, right = l.split(" -> ")
    pairs[left]=right

for turn in range(10):
    nextPoly = ""
    for i in range(len(polymer)-1):
        letter = polymer[i]
        pair = letter + polymer[i+1]
        nextPoly += polymer[i]+ pairs[pair]
    nextPoly += polymer[-1]
    polymer = nextPoly

c = Counter(polymer)
ordered = c.most_common() 
print(ordered)
print(ordered[0][1]- ordered[-1][1])