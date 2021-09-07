def generateParenthesis(n):
    res = []
    recur(n*2, res, '')

def is_valid(seq):
    st = []

    for s in seq:
        if s==')':
            if st==[]:
                return False 
            else:
                st.pop()
        else:
            st.append(s)

    if st==[]:
        return True 
    return False

def recur(n, res, curr):
    if n==0:
        if is_valid(curr):
            res.append(curr)
        return 

    recur(n-1, res, curr+')')
    recur(n-1, res, curr+'(')

n = 3

