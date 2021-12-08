with open("input.txt") as file: lines = file.read().splitlines()

def removeChars(string, chars):
    for c in chars:
        string = string.replace(c, "")
    return string
    
def commonChars(strings):
    common=set(strings[0])
    for i in range(1,len(strings)):
        common = common&set(strings[i])
    return "".join(list(common))

decodedOutputs=[]

for l in lines:
    codes, output = l.split(" | ")
    codes = codes.split()
    output = output.split()

    len5s=[]
    len6s=[]
    for c in codes:
        size = len(c)
        if size==2:
            len2=c
        elif size==3:
            len3=c
        elif size==4:
            len4=c
        elif size==5:
            len5s.append(c)
        elif size==6:
            len6s.append(c)

    a = removeChars(len3, len2)
    db = removeChars(len4, len2)
    adg = commonChars(len5s)
    d = commonChars([adg, db])
    b = removeChars(db, d)
    g = removeChars(adg, a+d)
    abfg = commonChars(len6s)
    f = removeChars(abfg, a+b+g)
    c = removeChars(len2, f)
    e = removeChars("abcdefg", a+b+c+d+f+g)

    zero = a+b+c+e+f+g
    two = a+c+d+e+g
    three = a+c+d+f+g
    five = a+b+d+f+g
    six = a+b+d+e+f+g
    nine = a+b+c+d+f+g
    
    decoded=""
    for n in output:
        nSize=len(n)
        if  nSize==2:
            decoded+="1"
        elif nSize==3:
            decoded+="7"
        elif nSize==4:
            decoded+="4"
        elif nSize==7:
            decoded+="8"
        elif all(x in n for x in zero):
            decoded+="0"
        elif all(x in n for x in six):
            decoded+="6"
        elif all(x in n for x in nine):
            decoded+="9"
        elif all(x in n for x in two):
            decoded+="2"
        elif all(x in n for x in three):
            decoded+="3"
        elif all(x in n for x in five):
            decoded+="5"
        else:
            print("shit happened")
    # print(decoded)
    decodedOutputs.append(decoded)

print(sum(list(map(int, decodedOutputs))))