from copy import deepcopy
with open("input") as file:lines = file.read().splitlines()

_, mask = lines[0].split(" = ")
size=len(mask)

def doMask(mask, num):
    binary=str(bin(num))[2:].zfill(size)
    result=[]

    for i in range(size):
        if (mask[i]=="X"):
            result.append(binary[i])
        else:
            result.append(mask[i])
    
    return "".join(result)

memo={}
for i in range(1,len(lines)):
    left, num = lines[i].split(" = ")
    if (left=="mask"):
        mask=num
        continue
    num=int(num)
    pos = int(left[4:-1])
    
    masked = doMask(mask, num)
    memo[pos]=int(masked,2)

#print(memo)
print("PART 1: ",sum(memo.values()))


# Part 2

def doMask2(mask, num):
    binary=str(bin(num))[2:].zfill(size)

    result=[[]]
    def addToResult(maskedNum, res=result):
        for r in res:
            r.append(maskedNum)

    for i in range(size):
        if (mask[i]=="0"):
            addToResult(binary[i])
        elif (mask[i]=="1"):
            addToResult("1")
        elif (mask[i]=="X"):
            copy1 = deepcopy(result)
            addToResult("0")
            addToResult("1", copy1)
            result += copy1

    finalResult=[]
    for r in result:
        finalResult.append("".join(r))
    return finalResult


memo2={}
for i in range(len(lines)):
    left, num = lines[i].split(" = ")
    if (left=="mask"):
        mask=num
        continue
    num=int(num)
    pos = int(left[4:-1])
    
    masked = doMask2(mask, pos)
    for m in masked:
        memPos = int(m, 2)
        memo2[memPos] = num
        
#print(memo2)
print("PART 2: ",sum(memo2.values()))
