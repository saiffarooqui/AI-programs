#8 puzzle
import copy
def getindex(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return [i,x.index(v)]

def heuristic(state):
    h=0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x,y=getindex(goal,state[i][j])
                #print(x,y)
                h+=abs(i-x)+abs(j-y)
    return h            

def isvalid(x,y):
    if x<=2 and x>=0 and y<=2 and y>=0:
        return True
    else:
        return False
    
def removeSeen(newstates, pqueue, visited, cur):
    npq=[state[0] for state in pqueue]
    vis=[state[0] for state in visited]
    result=[]
    for state in newstates:
        if (state in npq) or (state in vis):
            continue
        nodeT=[state, cur, heuristic(state)]
        result.append(nodeT)
    return result
    
def findLink(child, closed):
    if child == closed[0][0]:
        return closed[0]
    else:
        return findLink(child, closed[1:])

def reconstructPath(nodeTriple,closed):
    path = []
    #print("nodeTriple",nodeTriple)
    p,q,r=nodeTriple
    path.append(p)
    parent = q
    while parent is not None:
        path.append(parent)
        nodeTriple = findLink(parent, closed)
        p,q,r = nodeTriple
        parent = q
    return path 
    
def best_first_search():
    h=heuristic(ini_state)
    #print(h)
    pqueue=[[ini_state,None,h]]
    visited=[]
    while len(pqueue)>0:
        nodeTriple=pqueue[0]
        pqueue=pqueue[1:]
        cur,par,h=nodeTriple
        # print(cur,par,h)
        if cur==goal:
            return reconstructPath(nodeTriple,visited)
        else:
            visited=visited+[nodeTriple]
            #moveGen
            newstates=[]
            oldx,oldy=getindex(cur,0)
            #print(oldx,oldy)
            #move up
            newx=oldx-1
            newy=oldy
            #print("new",newx,newy)
            if isvalid(newx,newy):
                tempstate=copy.deepcopy(cur)
                #print("cur",tempstate)
                temp=tempstate[newx][newy]
                tempstate[newx][newy]=tempstate[oldx][oldy]
                tempstate[oldx][oldy]=temp
                newstates.append(tempstate)
            
            #move right
            #print(oldx,oldy)
            newx=oldx
            newy=oldy+1
            #print("new",newx,newy)
            if isvalid(newx,newy):
                tempstate=copy.deepcopy(cur)
                #print("cur",tempstate)
                temp=tempstate[newx][newy]
                tempstate[newx][newy]=tempstate[oldx][oldy]
                tempstate[oldx][oldy]=temp
                newstates.append(tempstate)
                
            #move left
            #print(oldx,oldy)
            newx=oldx
            newy=oldy-1
            #print("new",newx,newy)
            if isvalid(newx,newy):
                tempstate=copy.deepcopy(cur)
                #print("cur",tempstate)
                temp=tempstate[newx][newy]
                tempstate[newx][newy]=tempstate[oldx][oldy]
                tempstate[oldx][oldy]=temp
                newstates.append(tempstate)
                
            #move down
            #print(oldx,oldy)
            newx=oldx+1
            newy=oldy
            #print("new",newx,newy)
            if isvalid(newx,newy):
                tempstate=copy.deepcopy(cur)
                #print("cur",tempstate)
                temp=tempstate[newx][newy]
                tempstate[newx][newy]=tempstate[oldx][oldy]
                tempstate[oldx][oldy]=temp
                newstates.append(tempstate)    
            #print("newstates:",newstates)    
            
            noloops=removeSeen(newstates, pqueue, visited,cur)
        
            pqueue=pqueue+noloops
            # pqueue=sorted(pqueue,key=lambda item:item[2])
            pqueue.sort(key=lambda item:item[2])
            #print("pqueue:",pqueue)
    return False    
    

goal=[[1,2,3],[4,5,6],[7,8,0]]
ini_state=[[0,1,3],[4,2,5],[7,8,6]]
#ini_state=[[6, 0, 2], [1, 8, 4], [7, 3, 5]]
#goal=[[1, 2, 3], [8, 0, 4], [7, 6, 5]]
res=best_first_search()
if res:
    result=copy.deepcopy(res[::-1])
    print(len(result))
    for block in result:
        for row in block:
            print(row)
        print("----------------------------")    
else:
    print("No solution")
