def count_smaller(nums):

    counts = [0]*len(nums)
    idx_map = [(nums[i], i) for i in range(len(nums))]

    merge_sort_counts(idx_map, counts, 0, len(nums))

    return counts 

def merge_sort_counts(idx_map, counts, l, r):

    if r-l<=1:
        return

    mid = (l+r)//2

    merge_sort_counts(idx_map, counts, l, mid)
    merge_sort_counts(idx_map, counts, mid, r)

    return merge(idx_map, l, mid, r, counts)

def merge(idx_map, l, mid, r, counts):

    combo = []

    i = l
    j = mid

    while i<mid and j<r:
        if idx_map[i][0]<=idx_map[j][0]:
            counts[idx_map[i][1]] += j-mid
            combo.append(idx_map[i])
            i += 1
        else:
            combo.append(idx_map[j])
            j += 1
    
    while i<mid:
        counts[idx_map[i][1]] += j-mid
        combo.append(idx_map[i])
        i += 1

    while j<r:
        combo.append(idx_map[j])
        j += 1

    for i in range(l,r):
        idx_map[i] = combo[i-l]

nums = [7,2,5,4,1,6]
count_smaller(nums)

nums = [5,2,6,1]
count_smaller(nums)



    