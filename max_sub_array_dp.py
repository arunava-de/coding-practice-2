def max_sum_subarray(nums):

    if len(nums)==1:
        return nums[0]
        
    opt = [0]*len(nums)

    opt[0] = nums[0]
    opt[1] = max(opt[0]+nums[1], nums[1])
    
    for i in range(2,len(nums)):
        # opt[i] = max(max(opt[i-1]+nums[i], opt[i-2]), nums[i])
        opt[i] = max(opt[i-1]+nums[i], nums[i])

    return max(opt)
