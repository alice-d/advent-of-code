with open("input.txt") as file: lines = file.read().splitlines()

left = []
right = []
for l in lines:
    numbers = list(map(int, l.split()))
    left.append(numbers[0])
    right.append(numbers[1])

part2=0
for num in left:
    if num in right:
        part2 += right.count(num) * num

part1=0
while len(right) >0:
    minL = min(left)
    minR = min(right)
    left.remove(minL)
    right.remove(minR)

    part1 += abs(minL-minR)

print("Part 1: ", part1)
print("Part 2: ",part2)