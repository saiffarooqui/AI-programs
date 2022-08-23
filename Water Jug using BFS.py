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

def waterJug(x,y,z):
    if x>y:
        temp=x
        x=y
        y=temp
        
    queue=[[(0,0),None]]
    visited=[[(0,0),None]]
    
    while len(queue)>0:
        nodePair = queue.pop(0)
        p,q = nodePair
        a,b = p
        #goaltest
        if a==z or b==z:
            path = reconstructPath(nodePair, visited)
            return path

        states=[]
        #print(a, b)
        states.append([(x,b),(a,b)]) #fill jar x
        states.append([(0,b),(a,b)]) #empty jar x
        states.append([(a,y),(a,b)]) #fill jar y
        states.append([(a,0),(a,b)]) #empty jar y
        #print(states)
        states.append([(min(x,a+b), 0 if x>a+b else a+b-x),(a,b)]) #pour jar y to x
        states.append([(0 if y>a+b else a+b-y, min(y,a+b)),(a,b)]) #pour jar x to y
        for state in states:
            if any(state[0] == substate[0] for substate in visited):
                #print("check")
                continue
            queue.append(state)
            visited.append(state)            
    return False        
    
x = int(input("enter x: "))
y = int(input("enter y: "))
z = int(input("enter z: "))
res=waterJug(x,y,z)
if(x>y):
    print("Jug1: ",y,"Jug2: ",x)
else:
    print("Jug1: ",x,"Jug2: ",y)
if(res):
    print("Path Exists: ",end="")
    print(res[::-1])
else:
    print("No path exists")

    