import re
bagsContaing = {}

with open("input") as file:lines = file.read().splitlines()
for l in lines:
    bag, content = l.split(" bags contain ")
    innerBags = content.split(", ")

    colors = re.findall(r'[0-9]+ ([a-z ]+) bags?\.?', content)

    for c in colors:
        if c in bagsContaing:
            bagsContaing[c].append(bag)
        else:
            bagsContaing[c] = [bag]
# print(bagsContaing)

results = []

def addColorAndSearch(color):
    for bag in bagsContaing[color]:
        results.append(bag)
        if (bag in bagsContaing):
            addColorAndSearch(bag)

addColorAndSearch("shiny gold")
print(results)
print(len(set(results)))
