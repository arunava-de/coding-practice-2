class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def depth(node):
        
    d = 0
    while node.left:
        node = node.left 
        d += 1
        
    return d

def countNodes(root):
    
    if root==None:
        return 0
    
    d = depth(root)
    
    if d==0:
        return 1
    
    low = 1
    high = 2**d - 1
    
    while low<=high:
        
        mid = (low+high)//2
        
        if doesExist(mid, root, d):
            low = mid + 1
        else:
            high = mid -1
    
    return (2**d -1 + low)

def doesExist(idx, node, d):
    
    low = 0
    high = 2**d - 1
    
    i = 0
    
    while i<d:
        mid = (low+high)//2
        
        if idx<=mid:
            node = node.left
            high = mid
        else:
            node = node.right
            low = mid + 1
        i +=1
    
    return node!=None
        
            
