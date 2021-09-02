def count_inversions(nums):

    if len(nums)==1:
        return 0 

    return merge_count(nums)

def merge_count(nums):

    if len(nums)==1:
        return nums, 0
    elif len(nums)==2:
        if nums[1]<nums[0]:
            return [nums[1], nums[0]], 1
        else:
            return nums, 0

    mid = len(nums)//2

    left, cl = merge_count(nums[:mid])
    right, cr = merge_count(nums[mid:])

    combo, cc = merge(left, right)

    return combo, (cl + cr + cc)

def merge(left, right):

    i = 0
    j = 0
    c = 0

    out = [] 

    while i<len(left) and j<len(right):
        if left[i]<=right[j]: # Not an inversion
            out.append(left[i])
            i += 1
        else: # We have an inversion, all remaining elements of left are in first half, but greater than right[j]
            out.append(right[j])
            c += len(left) - i
            j += 1
    
    while i<len(left):
        out.append(left[i])
        i += 1

    while j<len(right):
        out.append(right[j])
        j += 1 

    return out, c 


nums = [1,2,3,4]
count_inversions(nums)

nums = [1,7,4,3]
count_inversions(nums)