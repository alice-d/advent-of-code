import re
bags = {}

with open("input") as file:lines = file.read().splitlines()
for l in lines:
    bag, content = l.split(" bags contain ")
    bags[bag] = []
    colors = re.findall(r'[0-9]+ ([a-z ]+) bags?\.?', content)
    numbers = re.findall(r'([0-9]+) [a-z ]+ bags?\.?', content)

    for i in range(len(colors)):
        bags[bag].append((int(numbers[i]), colors[i]))
# print(bags)

def howManyBags(color):
    inside = bags[color]
    count = 0
    for i in inside:
        count += i[0] + i[0] * howManyBags(i[1])
    return count

print(howManyBags("shiny gold"))
