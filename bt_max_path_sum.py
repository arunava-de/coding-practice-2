class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_max(node):

    if node==None:
        return 0 

    lmax = find_max(node.left)
    rmax = find_max(node.right)

    max_single = max(max(lmax, rmax) + node.val, node.val)

    max_sub = lmax + node.val + rmax 

    find_max.maxpath = max(max(max_single, max_sub), find_max.maxpath)
    
    return max_single # Sending this for parent call since we'll do max for other cases in parent function call 

def max_path_sum(root):

    find_max.maxpath = -10**9 
    find_max(root)

    return find_max.maxpath


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

max_path_sum(root)

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

max_path_sum(root)