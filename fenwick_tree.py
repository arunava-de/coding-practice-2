class FenwickTree:
    def __init__(self, arr, n):
        self.FT = [0]*(n+1)

        self.size = n+1

        for i in range(n):
            self.update_bit(i, arr[i])

    def update_bit(self, i, v):
        i += 1 

        while i<self.size:
            self.FT[i] += v
            i += i & (-i)

    def get_sum(self, i):
        i += 1 
        sum = 0

        while i>0:
            sum += self.FT[i]
            i -= i & (-i)

        return sum 
    
    def get_range(self, i, j):
        return self.get_sum(j) - self.get_sum(i-1)

arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
ftree = FenwickTree(arr, len(arr))

ftree.get_sum(5)
ftree.get_range(5,7)
