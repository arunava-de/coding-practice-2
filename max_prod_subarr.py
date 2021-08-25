def max_product(nums):
    n = len(nums)
    if n==1:
        return nums[0]

    opt = [0]*n
    mins = [0]*n
    opt[0] = nums[0]
    mins[0] = nums[0]

    for i in range(1,n):
        mins[i] = min(min(mins[i-1]*nums[i], opt[i-1]*nums[i]), nums[i])
        opt[i] = max(max(opt[i-1]*nums[i], mins[i-1]*nums[i]),nums[i])

    return max(opt)
