def find_kth_largest(nums, k):
    n = len(nums)

    if n==1:
        return nums[0]

    res = quickselect(nums, 0, n-1, n-k)
    return res 

def partition(s, e, nums):
    pivot = nums[s]
    idx = s

    while s<e:

        while s<len(nums) and nums[s]<=pivot:
            s += 1

        while nums[e]>pivot:
            e -= 1 

        if s<e:
            nums[s], nums[e] = nums[e], nums[s]

    nums[idx], nums[e] = nums[e], nums[idx]

    return e

def quickselect(nums, s, e, k):

    if s<e:
        pi = partition(s, e, nums)

        if pi==k:
            # print(nums[pi])
            return nums[pi]
        elif pi<k:
            return quickselect(nums, pi+1, e, k)
        else:
            return quickselect(nums, s, pi-1, k)
    else:
        return nums[s]

arr = [1,4,2,7,4,9]
k = 3
find_kth_largest(arr, k)




