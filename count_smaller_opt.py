from math import ceil, log2

class SegTree:
    def __init__(self, arr):
        
        n = len(arr)
        x = int(ceil(log2(n)))
        size = 2*(2**x) - 1

        self.ST = [None]*size 
        self.construct_seg_tree(arr, 0, n-1, 0)

    def construct_seg_tree(self, arr, s, e, si):

        if si<s or si>e:
            return 0 
        
        if s==e:
            self.ST[si] = arr[s]
            return arr[s]

        mid = (s+e)//2 

        self.ST[si] = self.construct_seg_tree(arr, s, mid, 2*si + 1) + self.construct_seg_tree(arr, mid+1, e, 2*si + 2)

        return self.ST[si]

    