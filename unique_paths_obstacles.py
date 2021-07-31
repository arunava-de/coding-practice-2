def unique_paths_obst(m, n, obs):

    M = [[0]*n for i in range(m)]

    if obs[m-1][n-1]==1:
        return 0
    f = 1
    for i in range(m):
        if obs[i][0]==1:
            f = 0
        M[i][0] = f

    f = 1
    for j in range(n):
        if obs[0][j]==1:
            f = 0
        M[0][j] = f

    for i in range(1,m):
        for j in range(1,n):
            if obs[i-1][j]==1 and obs[i][j-1]==0:
                M[i][j] = M[i][j-1]
            elif obs[i-1][j]==0 and obs[i][j-1]==1:
                M[i][j] = M[i-1][j]
            elif obs[i-1][j]==1 and obs[i][j-1]==1:
                M[i][j] = 0
            else:
                M[i][j] = M[i-1][j] + M[i][j-1]
    
    return M[m-1][n-1]