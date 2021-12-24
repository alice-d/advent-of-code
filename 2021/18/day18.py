#everything is done with strings, probably not a great solution
import math
import re
with open("input.txt") as file: lines = file.read().splitlines()

def shouldExplode(snail):
    size = len(snail)
    level=0
    explodeAt=None
    beforeDigitIndex=None
    for i in range(size):
        c = snail[i]
        if c=="[":
            level+=1
            if level==5:
                explodeAt=i
                break
        elif c=="]":
            level-=1
        elif c.isdigit():
            beforeDigitIndex=i
    return explodeAt, beforeDigitIndex

def findNumber(snail, startingPos):
    num=""
    foundNumber=False
    for i in range(startingPos, len(snail)):
        c = snail[i]
        if c.isdigit():
            num+=c
            foundNumber=True
        elif foundNumber:
            break
    return num, i-1

def findNumberBackwards(snail, start):
    num=""
    foundNumber=False
    for i in range(start, 0, -1):
        c = snail[i]
        if c.isdigit():
            num=c+num
            foundNumber=True
        elif foundNumber:
            break
    return num, i

def explode(snail, explodeAt, prevNumAt):
    afterExplode=""
    leftNum, _ = findNumber(snail, explodeAt+1)
    rightNum, righNumIndex = findNumber(snail, explodeAt+len(leftNum)+2)
    possibilySwitchingToZero=False

    #left side
    if prevNumAt==None:
        leftNum="0"
        possibilySwitchingToZero=True
        afterExplode+=snail[:explodeAt]
    else:
        leftLeft, leftLeftI = findNumberBackwards(snail, explodeAt-1)
        if prevNumAt==explodeAt-2:
            leftNum = str(int(leftLeft)+ int(leftNum))
            afterExplode+=snail[:leftLeftI+1] 
        else:
            lefLeftLen=len(leftLeft)
            leftLeft = str(int(leftLeft)+ int(leftNum))
            leftNum="0"
            possibilySwitchingToZero=True
            afterExplode+= snail[:leftLeftI+1] 
            afterExplode+= leftLeft 
            afterExplode+= snail[leftLeftI+lefLeftLen+1:explodeAt] 
    afterExplode += leftNum + ","

    #right side
    nextNum, nextNumAt = findNumber(snail, righNumIndex+1)
    if nextNum=="":
        rightNum="0"
        if possibilySwitchingToZero:
            afterExplode = afterExplode[:-2] + "0"  + snail[righNumIndex+2:] 
        else:
            afterExplode+=rightNum + snail[righNumIndex+2:] 
    elif nextNumAt==righNumIndex+3:
        rightNum = str(int(nextNum)+ int(rightNum))
        afterExplode+= rightNum + snail[nextNumAt+1:]
    else:
        rightRight = str(int(nextNum)+ int(rightNum))
        rightNum="0"
        if possibilySwitchingToZero:
            afterExplode = afterExplode[:-2] + "0"  
        else:
            afterExplode+= rightNum
        afterExplode+= snail[righNumIndex+2:nextNumAt-len(nextNum)+1]
        afterExplode+= rightRight + snail[nextNumAt+1:] 

    # print(afterExplode, "<- after explode") 
    return afterExplode

def hasBigNumber(snail):
    num=""
    bigNumI=None
    foundBig=False
    for i in range(len(snail)):
        c=snail[i]
        if c.isdigit():
            num += c
            bigNumI=i
            if len(num) > 1:
                foundBig=True
        elif not foundBig:
            num=""
        elif foundBig:
            return num, bigNumI
    return num, None

def split(snail, bigNum, bigNumI):
    afterSplit=snail[:bigNumI-1]
    bigNumInt=int(bigNum)
    half1  = str(bigNumInt//2)
    half2 = str(math.ceil(bigNumInt/2))
    afterSplit += "[" + half1 + "," + half2 + "]"
    afterSplit += snail[bigNumI+len(bigNum)-1:]
    # print(afterSplit, " <- after split")
    return afterSplit



def reduce(snail):
    while True:
        explodeAt, prevNumAt = shouldExplode(snail)
        if explodeAt!=None:
            snail = explode(snail, explodeAt, prevNumAt)
        else:
            bigNum, bigNumIndex = hasBigNumber(snail)
            if bigNum!="":
                snail = split(snail, bigNum, bigNumIndex)
            else:
                break
    # print(snail, "<- REDUCED")
    return snail

def magnitude(snail):
    p=re.compile("\[(\d+), *(\d+)\]")
    while "[" in snail:
        snail =p.sub(r'\1*3+\2*2', snail)
        snail =str(eval(snail))
    return snail

def sumSnails(first, sec):
    sum = "["+first+","+sec+"]"
    sum = reduce(sum)
    return sum


def doPart2():
    maxMag=0
    for l in lines:
        for i in range(len(lines)):
            if l == lines[i]: continue
            sum = sumSnails(l, lines[i])
            mag = int(magnitude(sum))
            if mag > maxMag:
                maxMag = mag
    print("Part 2 result: ", maxMag)

def doPart1():
    sum=lines[0]
    for i in range(1,len(lines)):
        sum = sumSnails(sum, lines[i])

    print("Part 1:")
    print(sum)
    print(magnitude(sum))

doPart1()
doPart2()