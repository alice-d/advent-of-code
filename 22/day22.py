from copy import copy, deepcopy
with open("input") as file: lines = file.read().splitlines()

player1 = []
player2 = []
p=1
for l in lines:
    if (p==2 and l.isdigit()):
        player2.append(int(l))
    elif (l.isdigit()):
        player1.append(int(l))
    elif (l==""):
        p+=1

print(player1)
print(player2)

def playGame(p1,p2):
    while (len(p1)>0 and len(p2)>0):
        next1 = p1[0]
        next2 = p2[0]
        p1=p1[1:]
        p2=p2[1:]
        if next1>next2:
            p1+=[next1, next2]
        else:
            p2+=[next2,next1]

    if (len(p1)==0):
        return p2
    else: 
        return p1

def score(deck):
    result=0
    points=len(deck)
    for card in deck:
        result+= card * + points
        points-=1
    print(result)

#part 1

deck = playGame(copy(player1),copy(player2))
score(deck)

#part 2

def playGameRec(p1,p2):
    history =[]
    while (len(p1)>0 and len(p2)>0):
        if [p1,p2] in history:
            return 1, p1
        else:
            history.append([p1,p2])

        next1 = p1[0]
        next2 = p2[0]
        p1=p1[1:]
        p2=p2[1:]

        if (len(p1)>= next1 and len(p2)>= next2):
            win, _ = playGameRec(p1[:next1],p2[:next2])
            if (win==1):
                p1+=[next1, next2]
            else:
                p2+=[next2,next1]

        elif next1>next2:
            p1+=[next1, next2]
        else:
            p2+=[next2,next1]

    if (len(p1)==0):
        return 2, p2
    else: 
        return 1, p1

print("PART 2")
_, deck = playGameRec(player1,player2)
score(deck)

