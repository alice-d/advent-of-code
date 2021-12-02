inp=input()
dic={}

while inp!="":
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

def calcPath(orbiter):
    path=[dic[orbiter]]
    orbitsAround=path[0]
    while orbitsAround!="COM":
        orbitsAround= dic[orbitsAround]
        path.append(orbitsAround)
    return path

youPath=calcPath("YOU")
#print(youPath)
santaPath =calcPath("SAN")
#print(santaPath)

def first_comon_element(list1, list2):
    for element in list1:
        if element in list2:
            return element

common = first_comon_element(youPath,santaPath)
#print(common)
common_until_com = len(calcPath(common))

print( len(youPath) - common_until_com + len(santaPath) - common_until_com - 2 )
