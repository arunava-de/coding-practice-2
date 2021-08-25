import math 

class DSet:

    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1]*n 
        self.sizes = [1]*n
    
    def find_compressed(self, idx):

        if self.parents[idx]==idx:
            return idx 
        
        self.parents[idx] = self.find_compressed(self.parents[idx])

        return self.parents[idx]

    def union_rank(self, idx1, idx2):

        p1 = self.find_compressed(idx1)
        p2 = self.find_compressed(idx2)

        if p1==p2:
            return

        if self.rank[p1]<self.rank[p2]:
            self.parents[p1] = p2 
            self.sizes[p2] += self.sizes[p1]
        elif self.rank[p1]<self.rank[p2]:
            self.parents[p2] = p1 
            self.sizes[p1] += self.sizes[p2]
        else:
            self.parents[p1] = p2 
            self.rank[p2] += 1
            self.sizes[p2] += self.sizes[p1]

def largestComponentSize(nums):
    n = len(nums)

    if n==1:
        return 1 

    dset = DSet(max(nums))

    for i in range(n):
        for k in range(2, math.sqrt(nums[i])):
            if nums[i]%k==0:
                dset.union_rank(nums[i], k)
                dset.union_rank(nums[i], nums[i]//k)

    max_size = 0
    groups = dict()

    for i in range(n):
        p = dset.find_compressed(nums[i])
        groups[p] += 1
        max_size = max(max_size, groups[p])

    return max_size

nums = [4,6,15,35]

nums = [20,50,9,63]

nums = [2,3,6,7,4,12,21,39]