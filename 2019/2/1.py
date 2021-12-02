inp=input()
while inp!="exit":
    l = list(map(int,inp.split(",")))
    print(l)
    for i in range (0,len(l),4):
        if l[i]==99:
            break
        res=0
        if l[i]==1:
            res= l[l[i+1]]+l[l[i+2]]
        elif l[i]==2:
            res= l[l[i+1]]*l[l[i+2]]
        else: 
            print("NOOPE")
            break
        l[l[i+3]]=res
    print(l)
    inp=input()