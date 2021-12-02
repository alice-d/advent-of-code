import math
inp="03036732577212944063491565474664"
originalPattern=[0, 1, 0, -1]
size=len(inp)
mul=int(math.ceil(size/len(originalPattern)))

bigPattern = originalPattern*(mul+1)

print(size)

def extend(num, pattern,size):
    newPat=[]
    stop=False
    for i in pattern:
        for j in range(num):
            newPat.append(i)
            if (len(newPat)==size+1):
                stop=True
                break
        if stop: break
    return newPat

for a in range(1000):
    res=[]
    for i in range(size):
        pat = extend(i+1,bigPattern,size)[1:] 
        #pat=pat[1:]
        summ=0
        for j in range(size):
            summ+=int(inp[j])*pat[j]

        res.append(str(abs(summ)%10))
        #res += abs(summ)%10 * 10**i

    print("After "+str(a+1)+" ")
    inp="".join(res)
    print(inp)

