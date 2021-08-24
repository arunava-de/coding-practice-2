from math import ceil, log2 

class SegTree:

    def __init__(self, n, arr):
        x = int(ceil(log2(n)))
        max_size = 2*(int(2**x)) - 1

        self.ST = [None]*max_size
        self.construct_seg_tree(arr, 0, n-1, 0)

    def construct_seg_tree(self, arr, s, e, i):
        if s==e:
            self.ST[i] = arr[s]
            return arr[s]
        
        mid = (s+e)//2 

        self.ST[i] = self.construct_seg_tree(arr, s, mid, 2*i+1) + self.construct_seg_tree(arr, mid+1, e, 2*i+2)

        return self.ST[i]

    def update_value(self, diff, i, s, e, si):

        if i<s or i>e:
            return 

        self.ST[si] += diff

        if s!=e:
        
            mid = (s+e)//2

            self.update_value(diff, i, s, mid, 2*si+1)
            self.update_value(diff, i, mid+1, e, 2*si+2)

    def get_sum(self, s, e, qs, qe, i):

        if qs<=s and qe>=e:
            return self.ST[i]
        
        if qe<s or qs>e: # Out of current range
            return 0

        mid = (s+e)//2

        return self.get_sum(s, mid, qs, qe, 2*i+1) + self.get_sum(mid+1, e, qs, qe, 2*i+2)

class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        self.segtree = SegTree(len(nums), nums)
        self.n = len(nums)
        
    def sumRange(self, left, right):
        
        return self.segtree.get_sum(0, self.n-1, left, right, 0)

    def update(self, index, val):

        diff = val - self.nums[index]
        self.nums[index] = val 

        self.segtree.update_value(diff, index, 0, self.n-1, 0)

nums = [1, 3, 5, 7, 9, 11]
sol = NumArray(nums)
sol.sumRange(1,3)
sol.update(1, 10)
sol.sumRange(1,3)