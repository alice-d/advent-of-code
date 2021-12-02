with open("input") as file: lines = file.read().splitlines()

def calculate(exp):
    exp=exp.replace(" ","")
    res=i=0
    op=""
    while i<len(exp):
        c=exp[i]
        if c in ["+","*"]:
            op=c
        elif c==")":
            return res,i+1
        else:
            if (c.isdigit()):
                rightArg = int(c)
            else:# c=="("
                rightArg, size = calculate(exp[i+1:])
                i=i+size

            if (op=="*"):
                res *= rightArg
            else:
                res += rightArg
        i+=1
    return res
         
s=0
for l in lines:
    s+=calculate(l)
print("Part 1: ",s)

# Part 2

def calculate2(exp):
    exp=exp.replace(" ","")
    res=i=0
    op=""
    while i<len(exp):
        c=exp[i]
        if c in ["+","*"]:
            op=c
            if (c=="*"):
                rightRes, size=calculate2(exp[i+1:])
                res*=rightRes
                i+=size
                if (exp[i])==")":
                    i-=1
        elif c==")":
            return res,i+1
        else:
            if (c.isdigit()):
                rightArg=int(c)
            else: # c=="(":
                rightArg, size=calculate2(exp[i+1:])
                i+=size

            if (op=="*"):
                res*=rightArg
            else:
                res+=rightArg
        i+=1
    return res,i

s=0
for l in lines:
    s+=calculate2(l)[0]
print("PART 2: ",s)