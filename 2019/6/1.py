inp=input()
dic={}

while inp!="":
    #print(inp)
    inp=inp.split(")")
    dic[inp[1]]=inp[0]
    inp=input()

orbitCount={}
for orbiter in dic:
    count=1
    orbitsAround=dic[orbiter]
    while orbitsAround!="COM":
        count+=1
        orbitsAround= dic[orbitsAround]
    orbitCount[orbiter]=count

total=0
for c in orbitCount:
    total+=orbitCount[c]

print(total)