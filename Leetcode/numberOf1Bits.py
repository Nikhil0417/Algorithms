class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #print(bin(n))
        s = str(bin(n))
        #print(s)
        c = s.count('1')
        #print(c)
        return c
