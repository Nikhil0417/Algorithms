import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)-k+1): #naive approach
            heapq.heapify(nums)
            #print(nums)
            a = heapq.heappop(nums)
            #print(a)
        return a
