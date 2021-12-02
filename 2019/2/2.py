def calculate(pointer,l):
    for i in range (pointer,len(l)-pointer,4):
        if l[i]==99:
            break
        res=0
        if l[i]==1:
            res= l[l[i+1]]+l[l[i+2]]
        elif l[i]==2:
            res= l[l[i+1]]*l[l[i+2]]
        else: 
            print("NOOPE")
            break
        l[l[i+3]]=res
    return l

inp=input()
pointer=0
while inp!="":
    initialList = list(map(int,inp.split(",")))
    currList=initialList[:]
    print(initialList)
    for noun in range(0,1):
        for verb in range(0,1):
            currList=initialList[:]
            currList[1]=noun
            currList[2]=verb
            print(currList)
            currList = calculate(pointer,currList)
            if currList[0]==19690720:
                print("sucess")
                print(currList)
                break
    inp=input()