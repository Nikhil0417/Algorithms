from heapq import heappush, heappop
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = list(set(nums))
        if(len(s)<3):
            return max(s)
        
        heap = []
        for i in range(len(s)):
            heappush(heap,s[i])
            if(len(heap)>3):
                heappop(heap)
        return heap[0]
