## Work in progress ##
from copy import copy, deepcopy
nums=[3,8,9,1,2,5,4,6,7]
#ex=[3,6,4,2,8,9,7,1,5]
#part 2
ex=copy(nums)
for i in range(10,1000001):
    ex.append(i)
#print(ex[:10],ex[-10:])
for i in range(10000000):#
    if (i%1000==0):print(i)
    curr =ex[0]
    next3 = ex[1:4]

    ex = ex[4:]
    num=curr-1

    while num!= curr:
        if (num in next3 +[curr] or num==1):
            if num<=1:
                num=1000000
            else:
                num-=1
        else:
            break
            
    destIndex = ex.index(num)
    ex = ex[:destIndex+1] + next3 + ex[destIndex+1:] +[curr]

    #print(ex[:10],ex[-10:])
one =  ex.index(1)

print(ex[one+1], ex[one+2])
print(ex[one+1] * ex[one+2])