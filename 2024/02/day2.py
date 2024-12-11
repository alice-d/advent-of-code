with open("input.txt") as file: lines = file.read().splitlines()

tryAgainReports = []

def saveLevelRemoved(firstRun, i, numbers):
    if (firstRun):
        copyWithoutCurrent = numbers.copy()
        del copyWithoutCurrent[i]
        copyWithoutPrev = numbers.copy()
        del copyWithoutPrev[i-1]
        copyWithoutFirst = numbers.copy()
        del copyWithoutFirst[0]
        tryAgainReports.append([copyWithoutCurrent, copyWithoutPrev, copyWithoutFirst])

def is_safe(numbers, firstRun=True):
    prev = numbers[0]
    incr = prev < numbers[1]
    safe = True

    for i in range(1, len(numbers)):
        n = numbers[i]
        diff = abs(prev - n)

        if (diff< 1 or diff > 3):
            saveLevelRemoved(firstRun, i, numbers)
            safe = False
            break

        if ((incr and prev > n) or (not incr and prev < n)):
            saveLevelRemoved(firstRun, i, numbers)
            safe = False
            break
        prev = n
    return safe

safe_n = 0
for l in lines:
    numbers = list(map(int, l.split()))
    safe = is_safe(numbers)

    if (safe):
        safe_n+=1
        print(numbers)
print("Part 1: ", safe_n)

def is_any_safe(versions):
    for nums in versions:
        if (is_safe(nums, False)):
            return True
    return False

for nums in tryAgainReports:
    if (is_any_safe(nums)):
        safe_n+=1

print("Part 2: ", safe_n)