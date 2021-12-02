inp=""
saved = []
with open("input.txt") as file: lines = file.read().splitlines()

horizontal = 0
depth = 0
for l in lines:
    direction, inc = l.split()
    inc =int(inc)
    if direction == "forward":
        horizontal += inc
    elif direction == "down":
        depth += inc
    else:
        depth-=inc


print(depth)
print(horizontal)
print(depth*horizontal)