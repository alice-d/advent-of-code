inp=""
saved = []
with open("input.txt") as file: lines = file.read().splitlines()
for l in lines:
    num = int(l)
    match = 2020 - num
    if (match in saved):
        print("Found: ", num, " + ", match)
        print("Result: ", num*match)
        break
    else:
        saved.append(num)