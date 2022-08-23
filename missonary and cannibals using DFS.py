def findLink(child, closed):
    if child == closed[0][0]:
        return closed[0]
    else:
        return findLink(child, closed[1:])

def reconstructPath(nodePair,closed):
    path = []
    p,q=nodePair
    path.append(p)
    parent = q
    while parent is not None:
        path.append(parent)
        nodePair = findLink(parent, closed)
        p,q = nodePair
        parent = q
    return path   

def removeSeen(states,stack,visited, parent):
    nstack=[s[0] for s in stack]
    nvis=[s[0] for s in visited]
    result=[]
    for n in states: 
        if (n in nstack) or (n in nvis):
            continue            
        else:
            result=result+[[n,parent]]
    return result

def MissCan(m,c):
    stack=[[[1,3,3],None]]
    visited=[]
    
    cases = [[-1,0],[0,-1],[-2,0],[0,-2],[-1,-1]]
    while len(stack)>0:
        #print("stack: ",stack)
        nodepair=stack[0]
        a,b=nodepair
        #print("nodepair: ",nodepair)
        if a==goal:
            return reconstructPath(nodepair,visited)
        else:
            #print("mac else")
            visited=visited+[nodepair]
            #print("visited:",visited)
            #movegen
            states=[]
            x,y = 0,0
            d = 0
            if a[0]==1:
                x,y,d = a[1],a[2],2
            else :
                x,y,d = 3-a[1],3-a[2],1
            for i in cases:
                nm1,nc1 = x + i[0],y + i[1]
                if d==1:
                    nm1,nc1 = 3-nm1, 3-nc1
               
                nm2,nc2 = 3-nm1,3-nc1
                if nm1<0 or nc1 <0 or (nm1!=0 and nm1<nc1) or (nm2!=0 and nm2<nc2):
                    continue
                #print("nm1,nc1: ",nm1,nc1)
                states.append([d,nm1,nc1])

            noloops=removeSeen(states, stack, visited,a)
 
            #new=makePair(noloops,a)

            stack=noloops+stack[1:]
            #print("stack:", stack)
       
    return False    
                               
goal=[2,0,0]
res=MissCan(3,3)
if(res):
    print("result:",res[::-1])
else:
    print("No solution")