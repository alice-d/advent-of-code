with open("input") as file:lines = list(map(int, file.read().splitlines()))

lines.sort()
dif3=dif1=0

#part 1
curr=0
for i in lines:
    if (i==curr+1):
        dif1+=1
    elif(i==curr+3):
        dif3+=1
    else:
        print("IDK: ",i)
    curr=i
dif3+=1
print(dif1,dif3)
print(dif1*dif3)

#part 2
mem ={}
lines.insert(0,0)
def store(num, pathCount):
    if (not(num in mem)):
        mem[num]=pathCount

def countPaths(i):
    num = lines[i]
    nextNums = lines[i+1:i+4]
    paths=0
    
    if (num in mem):
        return mem[num]

    for nextI in range(len(nextNums)):
        if (nextNums[nextI] <= num+3):
            paths += countPaths(i+nextI+1)

    if (num == lines[-1]):
        store(num, 1)
        return 1
    else:
        store(num, paths)
        return paths

print(countPaths(0))
#print(mem)

