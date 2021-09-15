def twoSum(nums, target):
        
    n = len(nums)
    
    if n==2:
        return [0,1]
    
    numsdict = {}
    
    for i in range(n):
        numsdict[nums[i]] = numsdict.get(nums[i], 0) + 1
        
    for i in range(n):
        curr = nums[i]
        if target-curr in numsdict:
            if target-curr==curr and numsdict[curr]>1:
                break
            elif target-curr!=curr:
                break
    
    for j in range(n):
        if target-curr==nums[j] and i!=j:
            return [i,j]