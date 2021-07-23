   
def is_safe(r, c, B):
    
    #Check same row left side
    
    for k in range(c):
        if B[r][k]=='Q':
            return False

    #Check principal diagonal left side
    
    k = 1
    
    while r-k>=0 and c-k>=0:
        if B[r-k][c-k]=='Q':
            return False
        k += 1
    
    #Check non-principal diagonal left side
    
    k = 1
    
    while r+k<len(B) and c-k>=0:
        if B[r+k][c-k]=='Q':
            return False
        k += 1
        
    return True

def placeQueens(B, c): #Placing queens column by column

    if c>=len(B):
        return 1

    res = 0

    for i in range(len(B)):

        if is_safe(i, c, B):
            B[i][c] = 'Q'

            res += placeQueens(B, c+1)
            
            B[i][c] = '.'
    
    return res 


def solveNQueens(n: int):
    
    B = [['.']*n for i in range(n)]
    return placeQueens(B, 0)
    

print(len(solveNQueens(4)))