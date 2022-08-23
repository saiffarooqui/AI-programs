def heuristic(state):
    h=0
    for i in range(n-1):
        for j in range(i+1,n):
            if abs((state[i]-state[j])/(i-j))==1:
                h+=1
    return h

def removeseen(newstates,pqueue,close):
    npq=[state[0] for state in pqueue]
    vis=[state[0] for state in close]
    result=[]
    for state in newstates:
        if (state in npq) or (state in vis):
            continue
        nodeP=[state,heuristic(state)]
        result.append(nodeP)
    return result

def bestfirstsearch():
    pqueue=[]
    close=[]
    h=heuristic(ini_state)
    state=[ini_state,h]
    pqueue.append(state)
    #print(pqueue)
    #sol=0
    while len(pqueue)>0:
        nodepair=pqueue[0]
        pqueue=pqueue[1:]
        a,b=nodepair
        #goal check
        if b==0:
            #sol+=1
            print("a: ",a)
            for i in range(n):
                for j in range(n):
                    if a[i]==j:
                        print("",j,"",end="")
                    else:
                        print(" - ",end="")
                print()
            return    
        else:
            close=close+[nodepair]
            #print(close)
            newstates=[]
            for i in range(1,n):
                tstate=a.copy()
                temp=a[i]
                tstate[0],tstate[temp]=tstate[temp],tstate[0]
                newstates.append(tstate)
        #print(newstates)
        noloops= removeseen(newstates,pqueue,close)
        pqueue=pqueue+noloops
        pqueue.sort(key=lambda item:item[1])
    return False    


n=int(input("Enter n: "))
ini_state=[]
for i in range(n):
    ini_state.append(i)
print("ini: ",ini_state)
#ini_state=[0,1,2,3,4,5,6,7]
bestfirstsearch()