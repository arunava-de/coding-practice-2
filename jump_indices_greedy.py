def can_jump(nums):
    
    if len(nums)==1:
        return True 

    curr_idx = 0

    while curr_idx<len(nums)-1:
        if nums[curr_idx]==0:
            return False 

        low = curr_idx + 1
        high = curr_idx + nums[curr_idx]

        if high>=len(nums)-1:
            return True 

        max_reachable = -float('inf')
        next_idx = -1

        for i in range(low, high+1):
            if nums[i]>max_reachable:
                max_reachable = nums[i]
                next_idx = i 
        
        curr_idx = next_idx 
    
    if curr_idx<len(nums)-1:
        return False 
    
    return True

nums = [2,3,1,1,4]
can_jump(nums)

nums = [1,1,1,1,1]
can_jump(nums)

nums = [3,2,1,0,4]
can_jump(nums)

nums = [0,0,0,0,5]
can_jump(nums)

nums = [4,0,0,0,5]
can_jump(nums)

nums = [5,9,3,2,1,0,2,3,3,1,0,0]
can_jump(nums)