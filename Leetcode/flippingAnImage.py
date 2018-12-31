class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = []
        for i in A:
            j = i[::-1]
            #print(j)
            a = []
            for k in j:
                if k==0:
                    x = 1
                else:
                    x = 0
                a.append(x)
            B.append(a)
        return B
