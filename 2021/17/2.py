# target area: x=20..30, y=-10..-5
# tXMin, tXMax, tYMin, tYMax = 20, 30, -10, -5
# target area: x=81..129, y=-150..-108
tXMin, tXMax, tYMin, tYMax = 81, 129, -150, -108

possibles=0
for velY in range(tYMin, 1000):
    for velX in range(tXMax+1):
        x=0
        dx=velX
        dy = velY
        y = 0
        while True:
            y+=dy
            dy-=1
            x+=dx
            dx -= 0 if dx==0 else 1

            if tYMin<=y<=tYMax and tXMin<=x<=tXMax:
                # print("reached target with vel ", velX, ", ", velY, " at step ", step)
                possibles+=1
                break
            elif y<tYMin or x>tXMax:
                break

print(possibles)