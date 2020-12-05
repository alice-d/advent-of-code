inp=""
saved = []
with open("input.txt") as file: 
    inp = file.readline()
    while inp != "":
        num = int(inp)
        match = 2020 - num
        if (match in saved):
            print("Found: ", num, " + ", match)
            print("Result: ", num*match)
            break
        else:
            saved.append(num)
        inp = file.readline()
print("done")