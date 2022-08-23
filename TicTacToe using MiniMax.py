def emptyCells(l):
    c = []
    for i in range(3):
        for j in range(3):
            if l[i][j]=='-':
                c.append([i,j])
    return c
def wins(l,c):
    states = [[l[0][0],l[0][1],l[0][2]],[l[1][0],l[1][1],l[1][2]],[l[2][0],l[2][1],l[2][2]],
    [l[0][0],l[1][0],l[2][0]],[l[0][1],l[1][1],l[2][1]],[l[0][2],l[1][2],l[2][2]],
    [l[0][0],l[1][1],l[2][2]],[l[2][0],l[1][1],l[0][2]]
    ]
    if [c,c,c] in states:
        return True
    else : return False
def evaluate(l):
    if wins(l,'O'):
        return 1
    elif wins(l,'X'):
        return -1
    return 0
def minmax(l,depth,player):
    best = []
    if depth==0 or wins(l,'O') or wins(l,'X'):
        return [-1,-1,evaluate(l)]
    if player=='O':
        best = [-1,-1,-1000]
    else:
        best = [-1,-1,1000]
    c = emptyCells(l)
    for i in c:
        r,cl = i[0],i[1]
        l[r][cl] = player
        score = []
        if player == 'O':
            score= minmax(l,depth-1,'X')
            score[0],score[1] = r,cl
            if best[2]<score[2]:
                best = score
        else:
            score= minmax(l,depth-1,'O')
            score[0],score[1] = r,cl
            if best[2]>score[2]:
                best = score
        l[r][cl] = '-'
    return best
l = [['-','-','-'] for _ in range(3)]
def printl(l):
    for i in l:
        print(i)
    print('*'*30)
turn= True
printl(l)
while 1:
    if turn:
        turn = not turn
        r,c = [int(i) for i in input().split()]
        l[r][c] = 'X'
        if wins(l,'X'):
            printl(l)
            print("you won")
            break
    else:
        turn = not turn
        nex = minmax(l,len(emptyCells(l)),'O')
        print(nex)
        if nex[0]==-1:
            print("draw")
            break
        else:
            l[nex[0]][nex[1]] = 'O'
            printl(l)
            if wins(l,'O'):
                printl(l)
                print("comp won")
                break