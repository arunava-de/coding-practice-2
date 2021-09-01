def countRangeSum(self, nums, lower, upper):
    if not nums:
        return 0
    
    n = len(nums)
    psum = [0]*n
    psum[0] = nums[0]
    
    for i in range(1, n):
        psum[i] = psum[i-1] + nums[i]
    
    def merge(lo, hi): # consist with the convention [lo:hi] ~ lo <= x < hi
        #print(lo, hi)
        mid = (lo+hi) // 2
        if lo == mid: 
            return int(lower<=psum[lo]<=upper) # there is only one elm, check if it is in [lower, upper]
        
        c = merge(lo, mid) + merge(mid, hi)
        #print(c)
        A = psum[lo:mid]
        
        i = j = mid
        for L in A:
            while i < hi and psum[i] < lower+L:
                i += 1
            while j < hi and psum[j] <= upper+L:
                j += 1
            c += (j - i)
        
        psum[lo:hi] = sorted(psum[lo:hi]) # one can improve this by merging two sorted arrays in linear time
        return c
    
    return merge(0, n)