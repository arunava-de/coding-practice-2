def topo_sort(u, visited, recstack, G):
    if u==None:
        return 
    
    visited.add(u)
    
    for v in G[u]:
        if v not in visited:
            topo_sort(v, visited, recstack, G)
    
    recstack.append(u)

def is_cyclic(u, visited, stack, G):

    stack.append(u)
    visited[u] = 0

    for v in G[u]:
        if visited[v]==-1:
            if is_cyclic(v, visited, stack, G):
                return True 
        elif visited[v]==0:
            return True 
    
    stack.pop()
    visited[u] = 1

    return False

def find_order(numCourses, prerequisites):

    if prerequisites==[]:
        # return list(range(numCourses))[::-1]
        print(list(range(numCourses))[::-1])

    G = dict()
    
    for i in range(numCourses):
        G[i] = set()
        
    for p in prerequisites:
        G[p[1]].add(p[0])

    #If cyclic, then courses can't be completed

    visited = {}
    for u in range(numCourses):
        visited[u] = -1
        
    stack = []

    for u in G.keys():

        if is_cyclic(u, visited, stack, G):
            # return []
            print([])

    stack = []
    visited = set()

    for u in G.keys():
        if u not in visited and G[u]!=set():
            topo_sort(u, visited, stack, G)

    for u in G.keys():
        if u not in stack: # No prerequisites
            stack.append(u)
            
    # return stack[::-1]
    print(stack[::-1])

test1 = [[0,1],[0,2],[1,2]]
n = 3

find_order(n, test1)

test2 = [[0,1]]
n = 3

find_order(n, test2)

