def calculate_arg(l,pointer,param):
    if param==0:
        return l[l[pointer]]
    else:
        return l[pointer]
def jump_cond(code,arg1):
    if ((arg1!=0 and code==5) or (arg1==0 and code==6)):
        return True
    else: return False

def comparison(code,arg1,arg2):
    if ((arg1<arg2 and code==7) or (arg1==arg2 and code==8)):
        return True
    else: return False
    
#inp=input()
inp = "3,8,1001,8,10,8,105,1,0,0,21,42,67,84,109,126,207,288,369,450,99999,3,9,102,4,9,9,1001,9,4,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,5,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99"
l = list(map(int,inp.split(",")))
def intcode(input1,input2):
    pointer=0
    while pointer < len(l)-1:
        command = l[pointer]
        opcode=command%100 #last 2 digits
        params = command//100
        param1 = params%10
        param2 = params//10%10
    
        if opcode==99:
            break
        res=0
    
        arg1=calculate_arg(l,pointer+1,param1)
        
        if opcode==3:
            #l[l[pointer+1]]=int(input())
            if (input1!=None):
                l[l[pointer+1]]=input1
                input1=None
            else:
                l[l[pointer+1]]=input2
            incr=2
        elif opcode==4:
            #print(arg1)
            return arg1
            incr=2
        else:
            arg2=calculate_arg(l,pointer+2,param2)
    
            if opcode==1 or opcode==2:
                if opcode==1:
                    res= arg1+arg2
                else:
                    res = arg1* arg2
                incr=4
                l[l[pointer+3]]=res
            
            elif opcode==5 or opcode==6:
                if (jump_cond(opcode, arg1)):
                    pointer=arg2
                    continue
                else:
                    incr=3
    
            elif opcode==7 or opcode==8:
                if (comparison(opcode,arg1,arg2)):
                    l[l[pointer+3]]=1
                else:
                    l[l[pointer+3]]=0
                incr = 4
                
            else: 
                print("NOOPE")
                break
        pointer += incr
        #print(l)     
    #print(l)
    
def repeatedDigits(a,b,c,d,e):
    fullNumber= str(a)+str(b)+str(c)+str(d)+str(e)
    if len(set(str(fullNumber))) < len(str(fullNumber)):
        return True
    else: return False
    
maxThr=-1
for a in range (0,5):
    for b in range (0,5):
        for c in range (0,5):
            for d in range (0,5):
                for e in range (0,5):
                    if repeatedDigits(a,b,c,d,e):
                        continue
                    outA=intcode(a,0)
                    outB=intcode(b,outA)
                    outC=intcode(c,outB)
                    outD=intcode(d,outC)
                    outE=intcode(e,outD)
                   # print(outE)
                    maxThr = max(maxThr, outE)
print(maxThr)
    