def split_array(nums, m):
    low = max(nums)
    high = sum(nums)
    ans = high

    while low<=high:
        mid = (low+high)//2

        count = split_into_groups(nums, mid)

        if count>m:
            low = mid+1
        else:
            ans = mid 
            high = mid-1

    return ans

def split_into_groups(nums, s):

    k = 0
    curr_group = 0

    for i in range(len(nums)):
        if nums[i]+curr_group>s:
            k += 1
            curr_group = nums[i]
        else:
            curr_group += nums[i]
    return k + 1

split_into_groups([1,2,4,3,2,7,8], 9)
split_into_groups([1,2,3,5,8,3,4], 9)


nums = [7,2,5,10,8]
m = 2
split_array(nums, m)

split_into_groups(nums, 15)