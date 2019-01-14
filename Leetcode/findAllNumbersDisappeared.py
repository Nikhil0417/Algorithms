from collections import defaultdict
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = defaultdict(int)
        for i in range(1,len(nums)+1):
            d[i] += 0
        l=[]
        for i in nums:
            d[i] += 1
        for i in d:
            if(d[i]==0):
                l.append(i)
        #print(d)
        #print(l)
        return l
        # O(n): time complexity and O(n): space complexity
