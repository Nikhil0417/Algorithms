class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        #print(A)
        for i in range(len(A)-1,1,-1):
            if(A[i-2]+A[i-1]>A[i]):
                return A[i-2]+A[i-1]+A[i]
        return 0
