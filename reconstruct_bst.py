class Node:

    def __init__(self, l=None, r=None, v=None):
        self.left = l
        self.right = r
        self.value = v

def reconstruct_tree(pre_list, in_list):
    if not in_list:
        return
    root = Node(None, None, pre_list.pop(0)) # First value always root
    root_index = in_list.index(root.value) # Find position of root in the inorder traversal
    root.left = reconstruct_tree(pre_list, in_list[:root_index]) # Left of root_index is left sub tree
    root.right = reconstruct_tree(pre_list, in_list[root_index+1:]) # Right of root_index is right sub tree
    return root 