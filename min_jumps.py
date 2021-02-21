def jump(nums):
    # Take a greedy approach. At any given position, evaluate all possible cells within reach and go for one with max value
    
    if len(nums)==1:
        return 0

    min_steps = 0

    i = 0

    while i<len(nums):
        reach = nums[i]
        if i+reach>=len(nums)-1:
            min_steps += 1
            break 
        
        local_max = i + reach
        local_ind = i
        for j in range(i+1,i+reach+1):
            if j + nums[j] > local_max:
                local_max = j + nums[j]
                local_ind = j
        
        i = local_ind
        min_steps += 1
        
    return min_steps

# nums = list(map(int,input().split()))
# print(nums)
nums = [10,9,8,7,6,5,4,3,2,1,1,0]
print(jump(nums))
