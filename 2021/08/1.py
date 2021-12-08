with open("input.txt") as file: lines = file.read().splitlines()

easy=0
for l in lines:
    _, output = l.split(" | ")
    nums = output.split()
    for n in nums:
        nSize=len(n)
        if  nSize==2 or nSize==3 or nSize==4 or nSize==7:
            easy+=1
print(easy)