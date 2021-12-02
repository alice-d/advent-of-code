def calculate_arg_pos(l,pointer,param,relative):
    arg =l[pointer]
    if param==0:
        return arg
    elif param==2:
        return relative + arg

def calculate_arg(l,pointer,param,relative):
    arg =l[pointer]
    if param==0:
        return l[arg]
    elif param==1:
        return arg
    elif param==2:
        return l[relative + arg]

def jump_cond(code,arg1):
    if ((arg1!=0 and code==5) or (arg1==0 and code==6)):
        return True
    else: return False

def comparison(code,arg1,arg2):
    if ((arg1<arg2 and code==7) or (arg1==arg2 and code==8)):
        return True
    else: return False
    
#inp=input()
inp = "3,8,1005,8,320,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,29,2,1005,1,10,1006,0,11,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,57,1,8,15,10,1006,0,79,1,6,3,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,90,2,103,18,10,1006,0,3,2,105,14,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,123,2,9,2,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,150,1,2,2,10,2,1009,6,10,1,1006,12,10,1006,0,81,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,187,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,209,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,231,1,1008,11,10,1,1001,4,10,2,1104,18,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,264,1,8,14,10,1006,0,36,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,293,1006,0,80,1006,0,68,101,1,9,9,1007,9,960,10,1005,10,15,99,109,642,104,0,104,1,21102,1,846914232732,1,21102,1,337,0,1105,1,441,21102,1,387512115980,1,21101,348,0,0,1106,0,441,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,209533824219,1,1,21102,1,395,0,1106,0,441,21101,0,21477985303,1,21102,406,1,0,1106,0,441,3,10,104,0,104,0,3,10,104,0,104,0,21101,868494234468,0,1,21101,429,0,0,1106,0,441,21102,838429471080,1,1,21102,1,440,0,1106,0,441,99,109,2,21201,-1,0,1,21101,0,40,2,21102,472,1,3,21101,0,462,0,1106,0,505,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,467,468,483,4,0,1001,467,1,467,108,4,467,10,1006,10,499,1102,1,0,467,109,-2,2106,0,0,0,109,4,2101,0,-1,504,1207,-3,0,10,1006,10,522,21101,0,0,-3,21202,-3,1,1,22101,0,-2,2,21102,1,1,3,21102,541,1,0,1106,0,546,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,569,2207,-4,-2,10,1006,10,569,22102,1,-4,-4,1105,1,637,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,588,1,0,1105,1,546,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,607,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,629,21201,-1,0,1,21102,629,1,0,105,1,504,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0"
l = list(map(int,inp.split(","))) + [0]*9999999

def intcode(pointer,relative,input1):
    #relative = 0
    #pointer=0
    while pointer < len(l)-1:
        #print(pointer)
        
        command = l[pointer]
        
        #print(command)
        opcode=command%100 #last 2 digits
        params = command//100
        param1 = params%10
        param2 = params//10%10
        param3 = params//100%10
    
        if opcode==99:
            break
        res=0
    
        arg1=calculate_arg(l,pointer+1,param1,relative)
        
        if opcode==3:
            pos = calculate_arg_pos(l,pointer+1,param1,relative)
            #l[pos]=int(input())
            l[pos]=input1
            incr=2

        elif opcode==4:
            #print(arg1)
            return [pointer +2,relative,arg1]
            incr=2

        elif opcode==9:
            relative+= arg1
            incr=2
            
        else:
            arg2=calculate_arg(l,pointer+2,param2,relative)
    
            if opcode==1 or opcode==2:
                pos = calculate_arg_pos(l,pointer+3,param3,relative)

                if opcode==1:
                    res= arg1+arg2
                else:
                    res = arg1* arg2
                incr=4
                l[pos]=res
            
            elif opcode==5 or opcode==6:
                if (jump_cond(opcode, arg1)):
                    pointer=arg2
                    continue
                else:
                    incr=3
    
            elif opcode==7 or opcode==8:
                pos = calculate_arg_pos(l,pointer+3,param3,relative)
                if (comparison(opcode,arg1,arg2)):
                    l[pos]=1
                else:
                    l[pos]=0
                incr = 4
                
            else: 
                print("NOOPE")
                break
        pointer += incr
        #print(l)     
    #print(l)
    return "end"

def calcDir(currDir,turn):
    if (currDir=="U"):
        if (turn==0):#left
            return "L"
        else: return "R"
    elif (currDir=="L"):
        if (turn==0):return "D"
        else:       return "U"
    elif (currDir=="D"):
        if (turn==0): return "R"
        else: return "L"
    else:#R
        if (turn==0): return "U"
        else:       return "D"

def calcPos(pos,dir):
    if (dir=="U"):
        return (pos[0],pos[1]+1)
    elif (dir=="D"):
        return (pos[0],pos[1]-1)
    elif (dir=="L"):
        return (pos[0]-1,pos[1])
    else:#R
        return (pos[0]+1,pos[1])
    return pos

currDir="U"
currPos = (0,0)
painting={(0,0): 1}
color=0
state=[]
pointer=0
relative=0
while True:
    if currPos in painting:
        color = painting[currPos]
    else:
        color = 0

    state=intcode(pointer,relative,color)
    if state=="end": break
    
    [pointer,relative,color]=state
    [pointer,relative,turnDir]=intcode(pointer,relative,color)


    painting[currPos]=color
    currDir = calcDir(currDir,turnDir)
    currPos = calcPos(currPos,currDir)



print(painting)
print(len(painting))

### part 2

minx=999
miny=999
maxx=-999
maxy=-999
for coord in painting:
    if (coord[0]>maxx):
        maxx=coord[0]
    elif (coord[0]<minx):
        minx=coord[0]
    if (coord[1]>maxy):
        maxy=coord[1]
    elif (coord[1]<miny):
        miny=coord[1]

xLen=maxx-minx+1
yLen=maxy-miny+1

actualPainting=[]
for i in range(yLen):
    actualPainting.append(" "*(xLen))

for coord in painting:
    if (painting[coord]==1):
        s=actualPainting[-coord[1]]
        newS = s[:coord[0]] + "X" +s[coord[0]+1:]
        actualPainting[-coord[1]] =newS

for layer in actualPainting:
    print(layer)








    