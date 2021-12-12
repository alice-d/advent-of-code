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
visited = ["start"]
def findPath(start, visited):
    # print("visiting ", start, ", came from ", visited)
    if (start=="end"):
        paths.append(visited)
        return
    for cave in graph[start]:
        if cave.isupper() or cave not in visited:
            findPath(cave, visited + [cave])

findPath("start", visited)
# print(paths)
print(len(paths))
