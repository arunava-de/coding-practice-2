def firstMissingPositive(nums):
    # There can only be a max of 300 elements
    # Hence we need to check if our list has the integers from 1 to 300

    exists = dict()
    for i in range(1,301):
        exists[i] = 0

    for i in range(len(nums)):
        if nums[i]>=1 and nums[i]<=300:
            exists[nums[i]] = 1

    for i in range(1,301):
        if exists[i] == 0:
            return i
    
    return 301

print(firstMissingPositive([-1,-4,0,-4,5]))

    