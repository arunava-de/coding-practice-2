class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Heap: # Modified to store heap on linkedlist nodes, not values
    def __init__(self, arr):
        self.heap = []
        self.N = 0
        self.build_heap(arr)

    def is_empty(self):
        return self.heap==[]
    
    def build_heap(self, arr):
        for v in arr:
            self.insert(v)

    def insert(self, v):
        self.heap.append(v)
        self.N += 1
        curr = self.N-1
        while curr>0:
            parent = (curr-1)//2
            if self.heap[parent].val > self.heap[curr].val:
                self.heap[parent], self.heap[curr] = self.heap[curr], self.heap[parent]
                curr = parent
            else:
                break 

    def delete_min(self):

        if self.is_empty():
            return

        target = self.heap[0]
        last = self.heap.pop()
        self.N -= 1

        if not self.is_empty():
            self.heap[0] = last 
            curr = 0

            while curr<self.N:
                if 2*curr+1>=self.N:
                    break
                cand = 2*curr+1
                if cand+1<self.N:
                    if self.heap[cand+1].val<self.heap[cand].val:
                        cand += 1
                if self.heap[curr].val>self.heap[cand].val:
                    self.heap[curr], self.heap[cand] = self.heap[cand], self.heap[curr]
                    curr = cand
                else:
                    break 

        return target

def merge(lists):

    k = len(lists)
    if k==0:
        return None
    elif lists==[None]*k:
        return None

    minheap = Heap(lists)
    head = None
    curr = None # Iterates through the list

    while not minheap.is_empty():
        min = minheap.delete_min()
        if head==None:
            head = min 
            curr = min 
        else:
            curr.next = min 
            curr = curr.next
        if min.next:
            minheap.insert(min.next)
        
    return head 

def list_to_LL(arr):

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

lists = [list_to_LL(l) for l in [[1,4,5],[1,3,4],[2,6]]]
