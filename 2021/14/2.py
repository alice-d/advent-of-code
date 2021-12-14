from collections import Counter
from copy import copy
with open("input.txt") as file: lines = file.read().splitlines()
polymer = lines[0]

pairs ={}
for l in lines[2:]:
    left, right = l.split(" -> ")
    pairs[left]=right

def incOrInsert(dict, key, inc):
    if key in dict:
        dict[key]+=inc
    else:
        dict[key]=inc

def decrement(dict, key, dec):
    if dict[key]-dec>0:
        dict[key]-= dec
    else:
        del dict[key]
    
currPolyPairs={}
for i in range(len(polymer)-1):
    letter = polymer[i]
    pair = letter + polymer[i+1]
    incOrInsert(currPolyPairs, pair, 1)

c = Counter(polymer)

for turn in range(40):
    copyPolyPairs = copy(currPolyPairs)
    for pair in copyPolyPairs:
        new = pairs[pair]
        quantity = copyPolyPairs[pair]
        
        incOrInsert(currPolyPairs, pair[0]+new, quantity)
        incOrInsert(currPolyPairs, new+pair[1], quantity)
        decrement(currPolyPairs, pair, quantity)
        c[new]+=quantity

ordered = c.most_common() 
print(ordered)
print(ordered[0][1]- ordered[-1][1])