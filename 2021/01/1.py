with open("input.txt") as file: lines = list(map(int, file.read().splitlines()))

prev = int(lines[0])
incs=0
for num in lines:
    if num > prev:
        incs+=1
    prev=num

print(incs)