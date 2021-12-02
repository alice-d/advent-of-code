inp=""
saved = []
with open("input.txt") as file: lines = file.read().splitlines()

horizontal = 0
depth = 0
aim = 0
for l in lines:
    direction, inc = l.split()
    inc =int(inc)
    if direction == "forward":
        horizontal += inc
        depth += aim * inc
    elif direction == "down":
        aim += inc
        #depth += inc
    else:#up
        aim -= inc
        # depth-=inc


print(depth)
print(horizontal)
print(depth*horizontal)