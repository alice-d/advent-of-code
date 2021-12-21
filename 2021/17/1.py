from copy import copy

# target area: x=20..30, y=-10..-5
# tXMin, tXMax, tYMin, tYMax = 20, 30, -10, -5
# target area: x=81..129, y=-150..-108
tXMin, tXMax, tYMin, tYMax = 81, 129, -150, -108

chosenPath=[]
for initialYVel in range(1000):
    step=1
    dy = initialYVel
    y = 0
    path=[0]
    while True:
        y+=dy
        path.append(y)
        step+=1
        dy-=1
        if tYMin<=y<=tYMax:
            # print("reached target with y vel ", initialYVel, " at step ", step)
            chosenPath=copy(path)
            break
        elif y<tYMin:
            break

print(max(chosenPath))
    
