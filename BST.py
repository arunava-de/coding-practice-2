class Node:

    def __init__(self, v, l=None, r=None):
        self.left = l
        self.right = r
        self.val = v

def inorder(root):
    if root == None:
        return ""
    if root.left == None and root.right == None:
        return "(" + str(root.val) + ")"
    return "(" + inorder(root.left) + str(root.val) + inorder(root.right) + ")"

def preorder(root):
    if root == None:
        return ""
    if root.left == None and root.right == None:
        return "(" + str(root.val) + ")"
    return "(" + str(root.val) + inorder(root.left) + inorder(root.right) + ")"

def postorder(root):
    if root == None:
        return ""
    if root.left == None and root.right == None:
        return "(" + str(root.val) + ")"
    return "(" + inorder(root.left) + inorder(root.right) +  str(root.val) + ")"

def search(root, key):
    if root.val == key:
        return root
    else:
        if key>root.val:
            return search(root.right, key)
        else:
            return search(root.left, key)

def insert(root, key):
    if root == None:
        return Node(key)
    if key<root.val:
        root.left =  insert(root.left, key)
    else:
        root.right =  insert(root.right, key)
    return root

def minLeaf(root):
    while root.left!=None:
        root = root.left
    return root

def delete(root, key):
    if root==None: # Nothing to delete
        return root
    if key<root.val:
        root.left = delete(root.left, key)
    elif key>root.val:
        root.right = delete(root.right, key)
    else: # We're at the node we want to delete
        if root.left == None:
            successor = root.right
            root = None
            return successor 
        if root.right == None:
            successor = root.left
            root = None 
            return successor
        # Both left and right child are present
        
        successor = minLeaf(root.right)
        root.val = successor.val
        root.right = delete(root.right, successor.val)
    return root
    
    
    

tree = Node(2)
tree.right = Node(5)
tree.left = Node(0)
tree.right.right = Node(6)
tree.right.left = Node(4)

print(search(tree, 4))
print(inorder(tree))