class Node:
    
    def __init__(self, v, nxt=None):
        self.val = v 
        self.next = nxt

def get_length(head):
    n = 0
    while head!=None:
        head = head.next
        n += 1

    return n 

def rotate_right(head, k):

    n = get_length(head)
    if n==0 or n==1:
        return head
    
    r = k%n #Effective number of rotations 
    
    if r==0:
        return head 

    rth = head 
    counter = n-r-1

    while counter>0:
        rth = rth.next 
        counter -= 1
    
    #rth will be the point where linked list is cutoff

    counter = n-1
    last = head 

    while counter>0:
        last = last.next
        counter -= 1

    new_head = rth.next 
    rth.next = None 

    last.next = head

    return new_head
    
l = [1,2,3,4,5]
head = Node(l[0])
curr = head

for i in range(1,5):
    temp = Node(l[i])
    curr.next = temp
    curr = curr.next