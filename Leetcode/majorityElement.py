from collections import defaultdict
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        for k in d:
            if(d[k]>int(len(nums)/2)):
                return k
