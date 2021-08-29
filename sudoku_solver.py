def find_next(grid):

    for i in range(9):
        for j in range(9):
            if grid[i][j]=='.':
                return [i,j]

    return False

def is_safe(grid, i, j, num):

    for x in range(9):
        if grid[x][j] == num:
            return False 

    for y in range(9):
        if grid[i][y] == num:
            return False 

    rstart = i - i%3 
    cstart = j - j%3 

    for x in range(3):
        for y in range(3):
            if grid[rstart+x][cstart+y] == num:
                return False 

    return True 

def recur(grid):

    next = find_next(grid)

    if not next:
        return True 
        # return

    i = next[0]
    j = next[1]

    for num in range(1,10):
        if is_safe(grid, i, j, str(num)):
            grid[i][j] = str(num)
            if recur(grid):
                return True 
                # return
            grid[i][j] = '.'

    return False
    # return

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

recur(board)
