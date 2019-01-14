from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        #print(d)
        l = []
        for i in d:
            l.append([d[i],i])
        #print(l)
        h = heapq.nlargest(k, l)
        result = []
        #print(h)
        for i in h:
            result.append(i[1])
        return result
            
