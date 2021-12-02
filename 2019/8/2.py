inp=""
with open("input.txt") as file:
	inp = file.readline()

segmentSize= 25*6

layers=[inp[i:i+segmentSize] for i in range(0,len(inp),segmentSize)]

image=""
for px in range(segmentSize):
    
    for l in range(len(layers)):
        color = layers[l][px]
        if color =="0" or color=="1":
            image+=color
            break
           
image=image.replace("0", " ")
image=image.replace("1", "X")
lines=[image[i:i+25] for i in range(0,len(image),25)] 
    
for i in lines:
    print(i)