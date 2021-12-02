with open("input") as file: lines = file.read().splitlines()

alergns = {}
allIngr=[]

def removeIngrEverywhereExcept(ingr, alergen):
    for a in alergns:
        if a!=alergen and ingr in alergns[a]:
            alergns[a].remove(ingr)

for l in lines:
    ingr, contains = l.split(" (contains ")
    contains = contains[:-1].split(", ")
    ingr = ingr.split()
    allIngr+=ingr

    for alerg in contains:
        if not(alerg in alergns):
            alergns[alerg] = ingr
        else:
            alergns[alerg] = list(set(alergns[alerg]).intersection(ingr))

        if len(alergns[alerg])==1:
            removeIngrEverywhereExcept(alergns[alerg][0], alerg)


allSafeIngr = list(filter(lambda a: not([a] in alergns.values()), allIngr ))
print(len(allSafeIngr))

response=""
for a in sorted(alergns):
    response+=alergns[a][0]+","
print(response[:-1])

