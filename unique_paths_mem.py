def unique_paths(m, n):
    
    M = [[0]*n for i in range(m)]

    for i in range(m):
        M[i][0] = 1

    for j in range(n):
        M[0][j] = 1

    for i in range(1,m):
        for j in range(1,n):
            M[i][j] = M[i-1][j] + M[i][j-1]

    return M[m-1][n-1]

