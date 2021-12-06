from collections import Counter
with open("input.txt") as file: lines = file.read().splitlines()

fishes = Counter(list(map(int, lines[0].split(","))))

for day in range(256):
    newFishes = fishes[0]
    for i in range(9):
        fishes[i] = fishes[i+1]
    fishes[6] +=newFishes
    fishes[8] +=newFishes

    # print(fishes)
print(sum(fishes.values()))