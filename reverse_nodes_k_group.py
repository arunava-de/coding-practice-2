# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. 
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create(self, arr):
        n = len(arr)
        i = 0
        head = None
        curr = None

        while i<n:
            if head==None:
                head = ListNode(arr[i])
                curr = head 
            else:
                curr.next = ListNode(arr[i])
                curr = curr.next
            i += 1
        
        return head 
    
    def print_list(self):
        while self!=None:
            print(self.val, end=" ")
            self = self.next

        print()

def reverse_util(head, k):
    prv = None 
    curr = head 
    nxt = head 

    while k>0:
        nxt = curr.next
        curr.next = prv 
        prv = curr 
        curr = nxt 
        k -= 1 

    return prv 
    
def reverse_k_group(head, k):

    curr = head 
    end = None 

    new_head = None

    while curr:
        count = 0
        curr = head 

        while count<k and curr:
            curr = curr.next
            count += 1
        
        if count==k:
            rev_head = reverse_util(head, k)

            if not new_head:
                new_head = rev_head
            
            if end: 
                end.next = rev_head

            end = head 
            head = curr 

    if end: # Need to attach the final portion, if exists
        end.next = head 
    
    return new_head if new_head else head

head = ListNode().create([1,2,3,4,5])
new_head = reverse_k_group(head, 2)
new_head.print_list()
