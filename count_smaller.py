def count_smaller(nums):

    counts = []

    for i in range(nums):
        c = 0
        for j in range(i+1,nums):
            if nums[j]<nums[i]:
                c += 1
        
        counts.append(c)

    return counts




