with open("input") as file:lines = file.read().splitlines()

when=int(lines[0])
buses= list(map(int,list(filter(lambda b: b!="x", lines[1].split(",")))))

wait=0
found=False
while not(found):
    for b in buses:
        if (when%b==0):
            found=True
            break
    else:
        wait+=1
        when+=1

print("part 1: ",wait*b)
print()

#part 2

#copy paste from somewhere
def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)
##

busesAll = lines[1].split(",")

big = max(buses)
when=0

bigIndex=busesAll.index(str(big))

busesWithIndexDiffs={}
indexDiffFromFirstAndBig=""

for i in range(len(busesAll)):
    if (busesAll[i]!="x"):
        if(int(busesAll[i])!=big):
            busesWithIndexDiffs[int(busesAll[i])] = -(bigIndex-i)
        if indexDiffFromFirstAndBig=="":
            indexDiffFromFirstAndBig=-(bigIndex-i)

#print(busesWithIndexDiffs)

found=set([big])
incr=big
while len(found)<len(buses):
    when+=incr
    #print(when)

    for b in busesWithIndexDiffs:
        if ((when+busesWithIndexDiffs[b])%b==0):
            found.add(b)
            incr=lcm(incr,b)
        else:
            break

print("part 2: ",int(when+indexDiffFromFirstAndBig))