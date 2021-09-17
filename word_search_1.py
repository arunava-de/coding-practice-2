def neighbors(i, j, m, n, board):

    x = [0, 0, 1, -1]
    y = [1, -1, 0, 0]
    res = []

    for k in range(4):
        cand = (i+x[k], j+y[k])
        if cand[0]<0 or cand[1]<0 or cand[0]>m-1 or cand[1]>n-1 or board[cand[0]][cand[1]]=='*':
            continue 
        res.append(cand)
    return res 

def exist(board, word):

    m = len(board)
    n = len(board[0])

    if m==1 and n==1:
        if len(word)>1:
            return False 
        if word[0]==board[0][0]:
            return True 
        else:
             False

    def recur(curr, i, j, k, board): # Here board[i][j] = word[k]
        nonlocal word
        nonlocal m 
        nonlocal n 
        
        if curr==word:
            return True 
        if k>=len(word):
            return False

        nbrs = neighbors(i, j, m, n, board)

        for nbr in nbrs:
            if board[nbr[0]][nbr[1]]==word[k]:
                board[nbr[0]][nbr[1]] = '*'
                if recur(curr+word[k], nbr[0], nbr[1], k+1, board):
                    return True
                board[nbr[0]][nbr[1]] = word[k]
        
        return False 
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                board[i][j] = '*'
                if recur(word[0], i, j, 1, board):
                    return True 
                board[i][j] = word[0]

    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
exist(board, word)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
exist(board, word)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
exist(board, word)

board = [['a','a']]
word = "aaa"
exist(board, word)
        