class Heap:
    def __init__(self):
        self.heap = []
        self.N = 0
    
    def is_empty(self):
        return self.heap==[]

    def get_min(self):
        return self.heap[0]

    def insert(self, v):
        self.heap.append(v)
        self.N += 1 
        curr = self.N-1

        while curr>0:
            parent = (curr-1)//2
            if self.heap[parent]>=self.heap[curr]:
                self.heap[parent], self.heap[curr] = self.heap[curr], self.heap[parent]
                curr = parent 
        
    def deletemin(self):
        if self.is_empty():
            return 

        val = self.heap[0]
        last = self.heap.pop()
        self.N -= 1

        if not self.is_empty():
            self.heap[0] = last
            curr = 0

            while curr<self.N:
                if 2*curr+1>=self.N:
                    break 

                cand = 2*curr+1 

                if cand+1<self.N and self.heap[cand+1]<self.heap[cand]:
                    cand += 1
                
                if self.heap[curr]>=self.heap[cand]:
                    self.heap[curr], self.heap[cand] = self.heap[cand], self.heap[curr]
                    curr = cand 
                else:
                    break 

        return val 

def min_meeting_rooms(intervals):
    n = len(intervals)
    if n==1:
        return 1 

    intervals.sort(key=lambda x:x[0])
    meeting_end = Heap() # Stores earliest time when a meeting room frees up 
    meeting_end.insert(intervals[0][1])

    for i in range(1,n):
        if meeting_end.is_empty():
            meeting_end.insert(intervals[i][1])
            continue
        if intervals[i][0]<meeting_end.get_min(): # We have a conflict
            meeting_end.insert(intervals[i][1])
        else:
            meeting_end.deletemin()
            meeting_end.insert(intervals[i][1])

    return meeting_end.N
    
intervals = [[0,30],[5,10],[15,20]]
min_meeting_rooms(intervals)

intervals = [[7,10],[2,4]]
min_meeting_rooms(intervals)

intervals = [[5,8],[6,8]]
min_meeting_rooms(intervals)