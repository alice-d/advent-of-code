valid=0
with open("input") as file: lines = file.read().splitlines()
for l in lines:
    policy, passw = l.split(": ")
    limits, letter = policy.split()
    pos1, pos2 = map(int,limits.split("-"))
    pos1-=1
    pos2-=1

    if ((passw[pos1]==letter and passw[pos2]!=letter) or (passw[pos1]!=letter and passw[pos2]==letter)):
        valid+=1

print(valid)