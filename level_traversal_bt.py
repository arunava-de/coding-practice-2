class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

def level_order_traversal(root):

    if root==None:
        return []

    out = []
    l = 0

    Q = [root]

    while Q:
        out.append([])
        lev_len = len(Q)

        for i in range(lev_len):
            u = Q.pop(0)

            out[-1].append(u)

            if u.left:
                Q.append(u.left)
            if u.right:
                Q.append(u.right)

        l += 1

    return out 