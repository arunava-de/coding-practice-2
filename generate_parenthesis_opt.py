def generateParenthesis(n):
    res = []
    recur(n*2, res, '', 0, 0, n)
    
    return res

def recur(n, res, curr, op, cl, mx):
    if n==0:
        res.append(curr)
        return 
    
    if op<mx:
        recur(n-1, res, curr+'(', op+1, cl, mx)
    if cl<op:
        recur(n-1, res, curr+')', op, cl+1, mx)
