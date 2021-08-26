class Node:
    def __init__(self, v, l, r):
        self.val = v
        self.left = l
        self.right = r 
    
def invert(root: Node):

    if root==None:
        return 
    
    if root.left:
        invert(root.left)
    if root.right:
        invert(root.right)

    root.left, root.right = root.right, root.left 

    return root