class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        d = dict()
        for i in S:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for j in J:
            if j in d:
                count += d[j]
        return count
        #faster than 8.74% of the submissions
