def min_path(M):

    m = len(M)
    n = len(M[0])

    opt = [[0]*n for i in range(m)]
    opt[0][0] = M[0][0]

    for i in range(1,m):
        opt[i][0] = M[i][0] + opt[i-1][0]

    for j in range(1,n):
        opt[0][j] = M[0][j] + opt[0][j-1]

    for i in range(1,m):
        for j in range(1,n):
            opt[i][j] = M[i][j] + min(opt[i-1][j],opt[i][j-1])

    return opt[m-1][n-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
min_path(grid)

grid = [[1,2,3],[4,5,6]]
min_path(grid)