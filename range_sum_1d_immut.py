class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefixes = []
        sum = 0
        for i in range(nums):
            sum = sum + nums[i]
            self.prefixes.append(sum)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        if left==0:
            return self.prefixes[right]

        return self.prefixes[right] - self.prefixes[left-1]

