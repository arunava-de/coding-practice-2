def merge_intervals(intervals):

    res = []

    if len(intervals)==1:
        return intervals

    intervals = sorted(intervals, key=lambda tup: tup[0])
    curr = intervals[0]

    for i in range(1, len(intervals)):
        next = intervals[i]
        if next[0]>curr[1]: #New interval starts after previous interval ends
            res.append(curr)
            curr = next
        else: # Overlap exists, so we merge the intervals
            curr[1] = max(curr[1], next[1])

    if curr not in res:
        res.append(curr)

    return res 

intervals = [[1,3],[2,6],[8,10],[15,18]]
merge_intervals(intervals)

intervals = [[1,4],[4,5]]
merge_intervals(intervals)

intervals = [[1,4],[0,4]]
merge_intervals(intervals)