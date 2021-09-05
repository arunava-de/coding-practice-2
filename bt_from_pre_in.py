class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right

def make_BT(preorder, inorder):

    def arr_to_tree(start, end):
        nonlocal preorder_idx

        if start>end:
            return 

        rootval = preorder[preorder_idx]
        root = TreeNode(rootval)

        preorder_idx += 1

        root.left = arr_to_tree(start, inorder_hash[rootval]-1)
        root.right = arr_to_tree(inorder_hash[rootval]+1, end)

        return root 

    preorder_idx = 0
    inorder_hash = {}

    for i in range(len(inorder)):
        inorder_hash[inorder[i]] = i 

    return arr_to_tree(0, len(inorder)-1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

root = make_BT(preorder, inorder)
