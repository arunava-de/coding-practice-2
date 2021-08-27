class Node:
    def __init__(self, x, nxt=None, rand=None):
        self.val = x
        self.next = nxt 
        self.random = rand 

visited = {}

def copy_random_list(head: Node):

    if head==None: 
        return 

    if head in visited:
        return visited[head]

    new = Node(head.val)

    visited[head] = new 

    new.next = copy_random_list(head.next)
    new.random = copy_random_list(head.random)
    
    return new