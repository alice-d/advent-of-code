r3=r1=r5=r7=d2=0
xR3=xR1=xR5=xR7=xD2=1

with open("input") as file: lines = file.read().splitlines()
xSize=len(lines[0])

def checkTree(x,y,r,counter):
    xScale=(x%xSize)-1
    if (lines[y][xScale]=="#"):
        counter+=1
    x+=r
    return x, counter

for y in range(len(lines)):

    if (y%2==0):
        xD2, d2 = checkTree(xD2,y,1,d2)

    xR1, r1 = checkTree(xR1,y,1,r1)
    xR3, r3 = checkTree(xR3,y,3,r3)
    xR5, r5 = checkTree(xR5,y,5,r5)
    xR7, r7 = checkTree(xR7,y,7,r7)

print(r1)
print(r3)#part 1 = 198
print(r5)
print(r7)
print(d2)

print(r1*r3*r5*r7*d2)
