count=0
currYes=set()
firstOfGroup=True

with open("input") as file: lines = file.read().splitlines()
for l in lines:
    if (l==""):
        count+=len(currYes)
        currYes=set()
        firstOfGroup=True
    else:
        if (firstOfGroup):
            currYes=set(l)
            firstOfGroup=False
        else:
            currYes=currYes.intersection(l)
        
count+=len(currYes)

print(count)