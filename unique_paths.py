def unique_paths(i, j, m, n):

    if i==m-1 and j==n-1:
        return 1

    if i==m-1 and j<n-1:
        return unique_paths(i, j+1, m, n)
    elif i<m-1 and j==n-1:
        return unique_paths(i+1, j, m, n)
    
    total = unique_paths(i, j+1, m, n) + unique_paths(i+1, j, m, n)
    return total 