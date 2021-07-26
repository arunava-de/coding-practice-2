def spiralize(M, rstart, rend, cstart, cend, elem):

    if rstart>rend or cstart>cend:
        return
    
    # Print first row
    for j in range(cstart, cend+1):
        M[rstart][j] = elem 
        elem += 1
    
    if rstart==rend: # Only one row
        return

    # Print last column, except first element
    for i in range(rstart+1, rend+1):
        M[i][cend] = elem
        elem += 1 
    
    if cstart==cend:
        return
        
    # Print last row, except last element
    for j in range(cend-1, cstart-1, -1):
        M[rend][j] = elem
        elem += 1
    
    # Print first column, except last and first element
    for i in range(rend-1, rstart, -1):
        M[i][cstart] = elem
        elem += 1

    return spiralize(M, rstart+1, rend-1, cstart+1, cend-1, elem)

def generate_matrix(n):

    M = [[0]*n for i in range(n)]
    spiralize(M, 0, n-1, 0, n-1, 1)

    return M