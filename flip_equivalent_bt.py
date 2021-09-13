class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left==None and self.right==None 

def flip_equivalent(root1, root2):
    
    def recur(r1, r2):
        
        if r1==None and r2==None:
            return True
        elif r1==None or r2==None:
            return False 

        if r1.val!=r2.val:
            return False 
        else:
            if r1.is_leaf() and r2.is_leaf():
                return True

        return (recur(r1.right, r2.right) or recur(r1.right, r2.left)) and (recur(r1.left, r2.right) or recur(r1.left, r2.left))

    return recur()
    



