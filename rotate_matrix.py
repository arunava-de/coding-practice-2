def rotate(matrix):

    if n==0:
        return []
    elif n==1:
        return matrix 
    # Take transpose
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print(matrix)

    # Do y reflection
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix