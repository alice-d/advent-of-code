start = [7,14,0,17,11,1,2]
dic = {}

prev=start[0]
for i in range(30000000):
    if (i<len(start)):
        dic[start[i]] = i
        prev = start[i]
    else:
        if prev in dic:
            diff = (i-1) - dic[prev]
        else:
            diff = 0
        dic[prev] = i-1
        prev = diff
    
    if (i in [2019, 29999999]):
        print("Turn ", i+1, " Num: ", prev)


