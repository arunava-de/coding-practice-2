def print_spiral(M, rstart, rend, cstart, cend, res):

    if rstart>rend or cstart>cend:
        return res
    
    # Print first row
    for j in range(cstart, cend+1):
        res.append(M[rstart][j])
    
    if rstart==rend: # Only one row
        return res

    # Print last column, except first element
    for i in range(rstart+1, rend+1):
        res.append(M[i][cend])
    
    if cstart==cend:
        return res
        
    # Print last row, except last element
    for j in range(cend-1, cstart-1, -1):
        res.append(M[rend][j])
    
    # Print first column, except last and first element
    for i in range(rend-1, rstart, -1):
        res.append(M[i][cstart])

    return print_spiral(M, rstart+1, rend-1, cstart+1, cend-1, res)

M = [[1,2,3],[4,5,6],[7,8,9]]
print_spiral(M, 0, 2, 0, 2, [])

M = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print_spiral(M, 0, 2, 0, 3, [])