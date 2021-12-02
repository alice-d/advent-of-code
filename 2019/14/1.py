import math
receita={}
with open("input.txt") as file:
    inp = file.readline()
    while inp!="":
        equation = inp.split(" => ")
        result = equation[1].split()
        ingredients=equation[0].split(",")
        elements={}
        for i in ingredients:
            elem = i.split()
            elements[elem[1]]=int(elem[0])

        receita[result[1]] = (int(result[0]),elements)       
        inp = file.readline()

fuelReq=receita["FUEL"][1]
print(fuelReq)
unused ={}
ores=0

def howManyOres(need, eq, currThing):
    global ores
    producing=eq[0]
    if (currThing in unused):
        sobras=unused[currThing]
        if (sobras > need):
            unused[currThing]-=need
            need=0
        else:
            need -= unused[currThing]
            unused[currThing]=0

    trade = math.ceil(float(need)/producing)
    
    for req in eq[1]:
        if (req=="ORE"):
            ores += trade*eq[1][req]
            #print("adding "+str(trade*eq[1][req])+" ores")
        else:
            howManyOres(eq[1][req]*trade,receita[req],req)
    
    left = (producing*trade) - need
    if (left>0):
        unused[currThing] = left

for req in fuelReq:
    howManyOres(fuelReq[req],receita[req], req)
fuel+=1

print(ores)