## Work in progress ##
import re
with open("ex") as file: lines = file.read().splitlines()


lonely_borders = {} #tile: [str,str]
neighors = {}#title: {R,L,B,T}


def checkNeighborAndAdd(border,currTile, currSide):
    print(neighors)
    print(border, currTile, currSide)
    found=False
    for tile in neighors:
        #print("for tile ",tile)
        theseBorders=neighors[tile]
        
        for side in theseBorders:
            #print("for side ",side)
            if theseBorders[side] in [border, border[::-1]]:
                theseBorders[side]=currTile
                neighors[currTile][currSide] = tile
                #print("for side break ")
                found=True
                break

    if not(found):
        #print("else, aka add")

        neighors[currTile][currSide]=border
                


tile=0
prevLine=""
curr_border_left=curr_border_right=""

def finishScanningTile(tile, prevLine, curr_border_left, curr_border_right):
    checkNeighborAndAdd(prevLine, tile, "B")
    checkNeighborAndAdd(curr_border_left, tile, "L")
    checkNeighborAndAdd(curr_border_right, tile, "R")
    #print(tile)
    #print(lonely_borders)
    

for l in lines:
    if tile==0:
        tile=int(re.search("Tile ([0-9]+):",l).group(1))
    elif l=="":
        finishScanningTile(tile, prevLine, curr_border_left, curr_border_right)
        curr_border_left=curr_border_right=""
        #if tile==1951:break
        tile=0
        
    else:
        if ("Tile" in prevLine):
            neighors[tile] ={}
            checkNeighborAndAdd(l, tile, "T")

        
            
        curr_border_left+=l[0]
        curr_border_right+=l[-1]
    prevLine=l
finishScanningTile(tile, prevLine, curr_border_left, curr_border_right)

for n in neighors:
    print(n, neighors[n])
