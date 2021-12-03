with open("input.txt") as file: lines = list(map(int, file.read().splitlines()))

prev = 999999999
incs=0
for i in range(1,len(lines)-1):
    soma = lines[i-1] + lines[i] + lines[i+1]
    if soma > prev:
        incs+=1
    prev=soma

print(incs)