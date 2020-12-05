valid=0
with open("input") as file: lines = file.read().splitlines()
for l in lines:
    policy, passw = l.split(": ")
    limits, letter = policy.split()
    mini, maxi = map(int,limits.split("-"))

    occurences = passw.count(letter)
    if (occurences>=mini and occurences<=maxi):
        valid+=1

print(valid)