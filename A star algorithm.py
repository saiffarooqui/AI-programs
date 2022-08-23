nodes=[]
h={} #heuristic
edges={}
weights={}
f={}
g={}

def belongs(node,li):
    for s in li:
        if node==s[0]:
            return True
    return False    

def removenode(node,li):
    for s in li:
        if s[0]==node:
            li.remove(s)
    return li        

def propagateImp(m):
    neigs=edges[m]
    for s in neigs:
        newG=g[m]+weights[m+s]
        if newG<g[s]:
            g[s]=newG
            f[s]=g[s]+h[s]
            if belongs(s,open):
                open=removenode(s,open)
                open.append([s,m,g[s],h[s],f[s]])
            if belongs(s,closed):
                closed=removenode(s,closed)
                closed.append([s,m,g[s],h[s],f[s]])
                propagateImp(s)

def findLink(child, closed):
    if child == closed[0][0]:
        return closed[0]
    else:
        return findLink(child, closed[1:])

def reconstructPath(state,closed):
    path = []
    path.append(state[0])
    parent = state[1]
    while parent is not None:
        path.append(parent)
        state = findLink(parent, closed)
        parent = state[1]
    return path               

def astar():
    g[start]=0
    f[start]=g[start]+h[start]
    state=[start,None,g[start],h[start],f[start]]   #[curr,par,g,h,f]
    open=[]
    open.append(state)
    closed=[]
    print("open: ",open)
    while len(open)>0:
        cur_state=open.pop(0)
        n=cur_state[0]
        closed.append(cur_state)
        print("open: ",open)
        print("closed: ",closed)
        if cur_state[0]==goal:
            print("Total cost: ",cur_state[2])
            return reconstructPath(cur_state,closed)
        else:
            neigs=edges[n]
            for m in neigs:
                if belongs(m,open)==False or belongs(m,closed)==False:
                    g[m]=cur_state[2]+weights[n+m]
                    f[m]=g[m]+h[m]
                    open.append([m,n,g[m],h[m],f[m]])
                elif belongs(m,open):
                    if (cur_state[2]+weights[n+m])<g[m]:
                        g[m]=cur_state[2]+weights[n+m]
                        f[m]=g[m]+h[m]
                        open=removenode(m,open)
                        open.append([m,n,g[m],h[m],f[m]])
                elif belongs(m,closed):
                    if (cur_state[2]+weights[n+m])<g[m]:
                        g[m]=cur_state[2]+weights[n+m]
                        f[m]=g[m]+h[m]
                        closed=removenode(m,closed)
                        closed.append([m,n,g[m],h[m],f[m]])
                        propagateImp(m)

        open.sort(key=lambda item:item[4])  
        print("open sorted: ",open)              

n=int(input("Enter number of nodes: "))
for i in range(n):
    nodes.append(input(f"Enter node {i+1}: ".upper()))
    h[nodes[i]]=float(input("Enter heuristic: "))
    edges[nodes[i]]=[]

s=d=""
cnt=0
print("Enter edges:")
print("To stop, enter 'end' for s and d: ")
while True:
    print("Enter edge",cnt+1)
    s=input("Enter source: ")
    d=input("Enter dest: ")
    if s=='end' and d=='end':
        break
    c=float(input("Enter edge cost: "))
    edges[s].append(d)
    edges[d].append(s)
    weights[s+d]=weights[d+s]=c 
    cnt+=1

start=input("Enter start node: ")
goal=input("Enter goal node: ")
print("nodes: ", nodes)
print("edges: ",edges)
print("h:",h)
print("f: ",f)
print("g:",g)
print("weights:", weights)

path=astar()
print(path[::-1])
