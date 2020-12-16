from copy import copy, deepcopy
with open("input") as file: lines = file.read().splitlines()

rules = {}
invalids = []
validTickets = []
myTicket = []
inputSection = 0

# Part 1
for l in lines:
    if l == "":
        inputSection += 1

    elif inputSection == 0:
        word, validRanges = l.split(": ")
        ranges = validRanges.split(" or ")
        newRule = []
        for r in ranges:
            rangee = list(map(int, r.split("-")))
            newRule.append(range(rangee[0], rangee[1] + 1))
        rules[word] = newRule

    elif inputSection == 1:
        if l != "your ticket:":
            myTicket = list(map(int, l.split(",")))

    else:
        if l != "nearby tickets:":
            ticketVals = list(map(int, l.split(",")))
            for num in ticketVals:
                for rule in rules.values():
                    if num in rule[0] or num in rule[1]:
                        break
                else:
                    invalids.append(num)
                    break
            else:
                validTickets.append(ticketVals)

print("Part 1: ", sum(invalids))


# Part 2
numValues = len(myTicket)
rulesOfTicketIndex = {}

for i in range(numValues):
    rulesOfTicketIndex[i] = list(rules.keys())

def removeRuleEverywhere(exceptNum, rulesOfCurrIndex, rule):
    rulesOfTicketIndex[exceptNum].remove(rule)

    if len(rulesOfCurrIndex) == 1:
        for j in rulesOfTicketIndex:
            if j != exceptNum and rulesOfCurrIndex[0] in rulesOfTicketIndex[j]:
                removeRuleEverywhere(j, rulesOfTicketIndex[j], rulesOfCurrIndex[0])

for t in validTickets:
    for i in range(numValues):
        theseRules = copy(rulesOfTicketIndex[i])
        for rule in theseRules:
            currRule = rules[rule]
            if t[i] not in currRule[0] and t[i] not in currRule[1]:
                removeRuleEverywhere(i, rulesOfTicketIndex[i], rule)

mul = 1
for r in rulesOfTicketIndex:
    if "departure" in rulesOfTicketIndex[r][0]:
        mul *= myTicket[r]
print("Part 2: ", mul)
