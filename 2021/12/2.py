with open("input.txt") as file: lines = file.read().splitlines()

graph={}
for l in lines:
    p1, p2 = l.split("-")
    
    for cave in [p1,p2]:
        if cave not in graph:
            graph[cave] = set()
        
    graph[p1].add(p2)
    graph[p2].add(p1)

print(graph)
        
paths=[]
def findPath(start, path, visitedSmallTwice):
    # print("visiting ", start, ", came from ", path)
    if (start=="end"):
        paths.append(path)
        return
    for cave in graph[start]:
        if cave.isupper() or cave not in path:
            findPath(cave, path + [cave], visitedSmallTwice)
        elif not visitedSmallTwice and cave!="start":
            findPath(cave, path + [cave], True)
        else: 
            continue
        
findPath("start", ["start"], False)
# for p in paths:
#     print(",".join(p))
print(len(paths))
