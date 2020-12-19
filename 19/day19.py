with open("input") as file: lines = file.read().splitlines()

rules={}

def matchesRules(msg, ruleNum, nextRules):
    if (msg==""):return False
    #print("matches ", msg, ruleNum, nextRules)

    rule = rules[ruleNum]
    if type(rule) is list:
        for possibleRule in rule:
            if matchesRules(msg, possibleRule[0], possibleRule[1:]+nextRules):
                return True  
        return False

    else:
        if msg[0]==rule:
            #print(msg[0], " checks out")
            if (len(nextRules)==0):
                if (len(msg)==1):
                    return True
                else:
                    return False
            return matchesRules(msg[1:],nextRules[0],nextRules[1:])
        else:
            return False


checkingMsgs=False
matches=0
for l in lines:
    if l=="":
        checkingMsgs=True

    elif not(checkingMsgs):
        ruleNum, rule = l.split(": ")
        ruleNum=int(ruleNum)

        if ('"' in rule):
            rules[ruleNum] = rule[1]
        
        else:
            rule =rule.split(" | ")
            ruleList=[]
            for r in rule:
                ruleList.append(list(map(int,r.split())))
            rules[ruleNum] = ruleList

    else:
        if (matchesRules(l,0,[])):  
            #print(l)
            matches+=1
        
print(matches)


