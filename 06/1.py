count=0
group=""

with open("input") as file: lines = file.read().splitlines()
for l in lines:
    if (l==""):
        count+=len(set(group))
        group=""
    else:
        group+=l
count+=len(set(group))

print(count)