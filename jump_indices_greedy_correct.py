def can_jump(nums):
    
    if len(nums)==1:
        return True 

    max_reachable = 0
    i = 0

    while i<len(nums) and i<=max_reachable:
        max_reachable = max(i+nums[i], max_reachable)
        i += 1

    if i==len(nums):
        return True 
    
    return False

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