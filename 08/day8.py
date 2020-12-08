with open("input") as file:lines = file.read().splitlines()

acc=i=0
visited=set()#indexes
numLines=len(lines)
while i not in visited:
    op, arg = lines[i].split()
    arg=int(arg)
    #print(i, op,arg)
    visited.add(i)

    if (op=="jmp"):
        i+=arg
    elif (op=="acc"):
        acc +=arg
        i+=1
    else:
        i+=1

    if (i>=numLines):
        print("Sucess")
        break
print(acc)        


#part2
organizedInfo={}
i=0
for l in lines:
    op, arg = l.split()
    arg=int(arg)
    organizedInfo[i]={"op": op, "arg": arg}
    i+=1

#search for ways to jump to an interval, if a reachable nop is found, that is the intruction that needs to change
def searchForWayToJumoToX(mini, maxi):
    indexes=[]
    for i in organizedInfo:
        if (organizedInfo[i]["op"]=="acc"):
            continue

        if (mini <= (i + organizedInfo[i]["arg"]) <= maxi):
            if (not(mini <= i < maxi)):
                if (organizedInfo[i]["op"]=="nop"):
                    if (reachable(i)):
                        print("CHANGE NOP to JMP", i, organizedInfo[i])
                        return True
                else:
                    #print(i,organizedInfo[i])
                    indexes.append(i)
    return indexes

def reachable(index):
    return index in visited

#search the previous intructions that do not jump away, if the jump before these is reachable, that needs to change to nop
def searchPrevInstructions(index):
    i=index-1
    indexes=[index]
    while True:
        if (organizedInfo[i]["op"]=="jmp"):
            if (not(0<organizedInfo[i]["arg"]<=len(indexes))):
                break
        indexes.append(i)
        i-=1

    if (reachable(i)):
        print("CHANGE JMP to NOP", i, organizedInfo[i])
        return True
    else:
        #print(indexes)
        return indexes

def reversePath(end):
    #print("Reverse path: ",end)
    prevs=searchPrevInstructions(end)
    if (prevs==True ):
        return
    jumps=searchForWayToJumoToX(prevs[-1],prevs[0])
    if (jumps!= True):
        for i in jumps:
            reversePath(i)
            
reversePath(numLines)

