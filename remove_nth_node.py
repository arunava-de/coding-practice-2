class Node:
    def __init__(self, v=0, nxt=None):
        self.val = v
        self.next = nxt 

def remove_nth(head, n):

    curr_node = head 
    prev_node = None 
    c = 1

    while c<n:
        prev_node = curr_node
        curr_node = curr_node.next
        c += 1

    next_node = curr_node.next 
    
    curr_node.next = None 
    prev_node.next = next_node 

    return head

head = Node(5)
head.next = Node(7)
head.next.next = Node(3)

head = remove_nth(head, 2)

while head!=None:
    print(head.val, end=" ")
    head = head.next