import statistics
from collections import Counter
with open("input.txt") as file: lines = file.read().splitlines()

crabs = list(map(int, lines[0].split(",")))

target = statistics.median(crabs)
print(target)

counter = Counter(crabs)
fuel=0
for pos in counter:
    fuel += (abs(target-pos))*counter[pos]

print(fuel)