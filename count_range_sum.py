from math import ceil, log2

class SegTree:
    def __init__(self, arr, lower, upper):
        
        n = len(arr)
        x = int(ceil(log2(n)))
        size = 2*(int(2**x)) - 1

        self.ST = [None]*size 
        self.construct_seg_tree(arr, 0, n-1, 0)

    def construct_seg_tree(self, arr, s, e, si):

        if s==e:
            self.ST[si] = arr[s]
            return arr[s]

        mid = (s+e)//2 

        left = self.construct_seg_tree(arr, s, mid, 2*si + 1)
        right = self.construct_seg_tree(arr, mid+1, e, 2*si + 2)

        self.ST[si] = left + right 

        return self.ST[si]
    
    def get_sum(self, s, e, qs, qe, i):

        if qs<=s and qe>=e:
            return self.ST[i]
        
        if qe<s or qs>e: # Out of current range
            return 0

        mid = (s+e)//2

        return self.get_sum(s, mid, qs, qe, 2*i+1) + self.get_sum(mid+1, e, qs, qe, 2*i+2)


def count_range_sum(nums, lower, upper):

    n = len(nums)
    if n==1:
        if nums[0]>=lower and nums[0]<=upper:
            return 1
        else:
            return 0

    segtree = SegTree(nums, lower, upper)
    count = 0 

    for i in range(n):
        for j in range(i,n):
            temp = segtree.get_sum(i,j)
            if temp>=lower and temp<=upper:
                count += 1
    
    return count