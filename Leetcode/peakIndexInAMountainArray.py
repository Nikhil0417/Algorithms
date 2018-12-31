class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = max(A)
        for i in range(len(A)):
            if A[i]==m:
                return i
