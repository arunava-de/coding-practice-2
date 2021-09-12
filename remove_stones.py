def remove_stones(stones):
    # Each stone is a node, two nodes have an edge between them iff either x-coordinate or y-coordinate matches
    n = len(stones)

    if n==1:
        return 0 
    
    G = {}
    for i in range(n):
        G[i] = set()
    
    X = {}
    Y = {}

    for i in range(n):
        pt = stones[i]

        if pt[0] not in X:
            X[pt[0]] = set([i])
        else:
            X[pt[0]].add(i)
        
        if pt[1] not in Y:
            Y[pt[1]] = set([i])
        else:
            Y[pt[1]].add(i)

    for i in range(n):
        pt = stones[i]
        G[i] = G[i].union(X[pt[0]])
        G[i] = G[i].union(Y[pt[1]])
        G[i].remove(i)
    
    # Now just need to find size of each connected component
    ccs = []
    visited = set()

    for i in range(n):
        if i not in visited:
            ccs.append(DFS(i, visited, G))

    return sum([c-1 for c in ccs])

def DFS(i, visited, G):

    S = [i]
    visited.add(i)
    comp = 1

    while S:
        u = S.pop()

        for v in G[u]:
            if v not in visited:
                visited.add(v)
                comp += 1
                S.append(v)
    
    return comp 

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
remove_stones(stones)

stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
remove_stones(stones)

stones = [[0,1],[1,0]]
remove_stones(stones)