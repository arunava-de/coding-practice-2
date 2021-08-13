def missing_ranges(nums, lower, upper):

    def format_range(l, u):
        if l==u:
            return str(l)
        return str(l) + "->" + str(u)

    misses = []
    prev = lower-1
    
    for i in range(len(nums)+1):
        curr = nums[i] if i<len(nums) else upper+1
        if prev+1<=curr-1:
            misses.append(format_range(prev+1, curr-1))
        prev = curr 

    return misses

missing_ranges([],-1,4)