class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        c = []
        for i in range(len(A[0])):
            r = []
            for j in range(len(A)):
                r.append(A[j][i])
                #print(r)
            c.append(r)
        return c
