class Node:
    def __init__(self, x, nxt=None, rand=None):
        self.val = x
        self.next = nxt 
        self.random = rand 

def get_node(node, visited):

    if node==None:
        return 

    if node in visited:
        return visited[node]
    
    new = Node(node.val)
    visited[node] = new 
    return new

def copy_random_list(head: Node):

    if head==None: 
        return 

    old_node = head
    new_node = Node(old_node.val)

    maps = {}
    maps[old_node] = new_node

    while old_node!=None:

        new_node.next = get_node(old_node.next)
        new_node.random = get_node(old_node.random)

        new_node = new_node.next
        old_node = old_node.next 

    return maps[head]