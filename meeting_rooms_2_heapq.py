import heapq
    
class Solution:
    
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n==1:
            return 1 

        intervals.sort(key=lambda x:x[0])
        meeting_end = [] # Stores earliest time when a meeting room frees up 
        heapq.heappush(meeting_end, intervals[0][1])

        for i in range(1,n):

            if intervals[i][0]>=meeting_end[0]: # We don't have a conflict
                heapq.heappop(meeting_end)
            heapq.heappush(meeting_end, intervals[i][1])

        return len(meeting_end)