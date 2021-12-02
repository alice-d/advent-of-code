inp=""
with open("input.txt") as file:
	inp = file.readline()

segmentSize= 25*6

byLayer=[inp[i:i+segmentSize] for i in range(0,len(inp),segmentSize)]


lessZeros=[0,len(byLayer[0])]

for l in byLayer:
    zeros = l.count("0")
    if zeros < lessZeros[1]:
        lessZeros[1]=zeros
        lessZeros[0]=l
    
print(lessZeros[0].count("1")*lessZeros[0].count("2"))