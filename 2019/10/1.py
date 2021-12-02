
inp=input()
asteroids =[]
y=0
while inp!="":
    for x in range(len(inp)):
        if (inp[x]=="#"):
            asteroids.append([y,x])
    y+=1
    inp=input()

print(asteroids)

from functools import reduce
def factors(n):    
    return set(reduce(list.__add__, 
            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

maxDetected=0
bestAst=[-1,-1]
for a in asteroids:
    #print(a)
    detects=0
    for other in asteroids:
        if other==a:
            continue
        found=False
        diff = [other[0]-a[0],other[1]-a[1]]
        if (abs(diff[0])==1 or abs(diff[1]==1)):
            found=False

        elif (abs(diff[0])==abs(diff[1])):
            ySignal=diff[1]//abs(diff[1])
            for i in range (ySignal,diff[1],ySignal):
                x = abs(i) * (diff[0]//abs(diff[0]))
                if( [a[0]+x,a[1]+i] in asteroids):
                    found=True
                    break

        elif (diff[0]==0):
            ySignal=diff[1]//abs(diff[1])
            for i in range (ySignal,diff[1],ySignal):
                if( [a[0],a[1]+i] in asteroids):
                    found=True
                    break
            
        elif (diff[1]==0):
            xSignal=diff[0]//abs(diff[0])
            for i in range (xSignal,diff[0],xSignal):
                if( [a[0]+i,a[1]] in asteroids):
                    found=True
                    break
  
        else:
            #equ: ax +by =c, a=diff1, b=-diff0
            aEq = diff[1]
            b = -diff[0]
            c=aEq*a[0]+b*a[1]
            #print(str(diff[1])+"*x + "+str(diff[0])+"*y = "+str(c))
            xSignal=diff[0]//abs(diff[0])
            ySignal=diff[1]//abs(diff[1])
            for xInc in range (xSignal,diff[0],xSignal):
                for yInc in range (ySignal,diff[1],ySignal):
                    x=a[0]+xInc
                    y=a[1]+yInc
                    if ( aEq*x + b*y == c):
                        if( [x,y] in asteroids):
                            found=True
        if (not found):
            detects+=1
            #print("canReach")
    #print("number of detected asteriods")
    #print(detects)
    if (detects > maxDetected):
        maxDetected=detects
        bestAst=a

print(bestAst)
print(maxDetected)



