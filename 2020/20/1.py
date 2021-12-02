import re
with open("input") as file: lines = file.read().splitlines()

lonely_borders = {} #tile: [str,str]

def checkNeighborAndAdd(border,currTile):
    for tile in lonely_borders:
        theseBorders=lonely_borders[tile]
        if border in theseBorders :
            theseBorders.remove(border)
            break
        elif border[::-1] in theseBorders:
            theseBorders.remove(border[::-1])
            break
    else:

        if currTile in lonely_borders:
            lonely_borders[currTile].append(border)
        else:
            lonely_borders[currTile] = [border]
                

tile=0
prevLine=curr_border_left=curr_border_right=""

def finishScanningTile(tile, prevLine, curr_border_left, curr_border_right):
    checkNeighborAndAdd(prevLine, tile)
    checkNeighborAndAdd(curr_border_left, tile)
    checkNeighborAndAdd(curr_border_right, tile)   

for l in lines:
    if tile==0:
        tile=int(re.search("Tile ([0-9]+):",l).group(1))

    elif l=="":
        finishScanningTile(tile, prevLine, curr_border_left, curr_border_right)
        curr_border_left=curr_border_right=""
        tile=0    

    else:
        if ("Tile" in prevLine):
            
            checkNeighborAndAdd(l, tile)
        curr_border_left+=l[0]
        curr_border_right+=l[-1]

    prevLine=l

finishScanningTile(tile, prevLine, curr_border_left, curr_border_right)

#print(lonely_borders)
mul=1
for tile in lonely_borders:
    if len(lonely_borders[tile])==2:
        mul*=tile
print(mul)
        