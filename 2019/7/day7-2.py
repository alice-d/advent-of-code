# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:12:09 2019

@author: Alice
"""

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

#inp="3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
#inp="3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
inp = "3,8,1001,8,10,8,105,1,0,0,21,42,67,84,109,126,207,288,369,450,99999,3,9,102,4,9,9,1001,9,4,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,5,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99"
l = list(map(int,inp.split(",")))

def intcode(input1,input2,pointer,li):
    #pointer=0
    while pointer < len(li)-1:
        command = li[pointer]
        opcode=command%100 #last 2 digits
        params = command//100
        param1 = params%10
        param2 = params//10%10
    
        if opcode==99:
            break
        res=0
    
        arg1=calculate_arg(li,pointer+1,param1)
        
        if opcode==3:
            if (input1!=None):
                li[li[pointer+1]]=input1
                input1=None
            else:
                li[li[pointer+1]]=input2
            incr=2
            
        elif opcode==4:
            return [arg1,pointer+2,li]
            incr=2
        else:
            
            arg2=calculate_arg(li,pointer+2,param2)
    
            if opcode==1 or opcode==2:
                if opcode==1:
                    res= arg1+arg2
                else:
                    res = arg1* arg2
                incr=4
                li[li[pointer+3]]=res
            
            elif opcode==5 or opcode==6:
                if (jump_cond(opcode, arg1)):
                    pointer=arg2
                    continue
                else:
                    incr=3
    
            elif opcode==7 or opcode==8:
                if (comparison(opcode,arg1,arg2)):
                    li[li[pointer+3]]=1
                else:
                    li[li[pointer+3]]=0
                incr = 4
                
            else: 
                print("NOOPE")
                break
        pointer += incr
    
def repeatedDigits(a,b,c,d,e):
    fullNumber= str(a)+str(b)+str(c)+str(d)+str(e)
    if len(set(str(fullNumber))) < len(str(fullNumber)):
        return True
    else: return False
    
def process_intcode(outs,pointers,lists,seq):
    for i in range(5):
        result=intcode(seq[i],outs[i-1],pointers[i],lists[i])
        
        if result!=None:
            [outs[i],pointers[i],lists[i]]=result
        else: return "end"
            
    return [outs,pointers,lists,[None]*5]

maxThr=0
for a in range (5,10):
    for b in range (5,10):
        for c in range (5,10):
            for d in range (5,10):
                for e in range (5,10):
                    
                    if repeatedDigits(a,b,c,d,e):
                        continue
                    
                    pointers=[0,0,0,0,0]
                    lists=[l[:],l[:],l[:],l[:],l[:]]
                    seq=[a,b,c,d,e]
                    outs=[0,0,0,0,0]
                    
                    while True:
                        result=process_intcode(outs,pointers,lists,seq)
                        
                        if (result=="end"):
                            break
                        [outs,pointers,lists,seq]=result
                    
                    maxThr = max(maxThr, outs[4])            
print(maxThr)
