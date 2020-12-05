inp=""
saved = []

def find_num_that_sums_to_x(savedOfThisSum, allTheNums, target, third):
    for curr in allTheNums:
        match = target - curr
        if (match in savedOfThisSum):
            print("Found: ", curr, " + ", match, "+", third)
            print("Result: ", curr*match*third)
            return True
        else:
            savedOfThisSum.append(curr)
    return False

with open("input.txt") as file: 
    inp = file.readline()
    while inp != "":
        num = int(inp)
        sumOf2 = 2020 - num
        if ( find_num_that_sums_to_x([],saved,sumOf2, num) ):
            break
        saved.append(num)
        inp = file.readline()
print("done")