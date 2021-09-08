# Split array into m subarrays and minimize sum of max sum subarray
def split_array(nums, m):

    n = len(nums)

    opt = [[float('inf')] * (m+1) for _ in range(n+1)]
    sums = [0]*(n+1)

    for i in range(n): # For the subarray sums in constant time
        sums[i+1] = sums[i] + nums[i]

    opt[0][0] = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            for k in range(i):
                opt[i][j] = min(opt[i][j], max(opt[k][j-1], sums[i]-sums[k]))

    return opt[n][m]

nums = [7,2,5,10,8]
m = 2
split_array(nums, m)