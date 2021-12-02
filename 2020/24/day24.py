## Work in progress (regarding part 2) ##
with open("input") as file: lines = file.read().splitlines()

blacks=[]

for l in lines:
    #last=""
    goingUpDown=False
    curr=[0,0]
    for direct in l:
        #if direct=="n" or direct=="s":
        #    last=direct
        #    continue
        #else: last=""
        #direction = last + direct
        inc=2
        if direct=="s":
            goingUpDown=True
            curr[1]-=inc
        elif direct=="n":
            goingUpDown=True
            curr[1]+=inc
        elif direct=="e":
            if (goingUpDown):
                inc=1
            curr[0]+=inc
            goingUpDown=False
        else:
            if (goingUpDown):
                inc=1
            curr[0]-=inc
            goingUpDown=False
   # print(curr)
    if curr in blacks:
        #print("flipped back")
        blacks.remove(curr)
    else:
        #print("flipped")
        blacks.append(curr)
print(blacks)
print(len(blacks))
