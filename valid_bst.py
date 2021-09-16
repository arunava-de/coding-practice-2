def is_valid(root):

    def valid_recur(root, lower, upper):
        if root==None:
            return True 

        if root.val<lower or root.val>upper:
            return False 

        if root.left and root.right:
            return valid_recur(root.left, lower, root.val-1) and valid_recur(root.right, root.val+1, upper)
        elif root.left:
            return valid_recur(root.left, lower, root.val-1)
        elif root.right:
            return valid_recur(root.right, root.val+1, upper)
        
        return True

    return valid_recur(root, -float('inf'), float('inf'))