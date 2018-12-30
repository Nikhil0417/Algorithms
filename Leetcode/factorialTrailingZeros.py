class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1,20):
            count += int(n/pow(5,i))
        return int(count)
