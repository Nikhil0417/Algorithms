class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum([i for i in range(len(nums)+1)])
        #print(s)
        return s-sum(nums)
