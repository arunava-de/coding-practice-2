class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right

def make_BT(inorder, postorder):

    def arr_to_tree(start, end):
        if start>end:
            return 

        rootval = postorder.pop()
        root = TreeNode(rootval)
        
        root.right = arr_to_tree(inorder_hash[rootval]+1, end)
        root.left = arr_to_tree(start, inorder_hash[rootval]-1)

        return root 

    inorder_hash = {}

    for i in range(len(inorder)):
        inorder_hash[inorder[i]] = i

    return arr_to_tree(0, len(inorder)-1)

postorder = [9,15,7,20,3]
inorder = [9,3,15,20,7]

root = make_BT(inorder, postorder)
