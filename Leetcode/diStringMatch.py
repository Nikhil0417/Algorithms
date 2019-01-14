class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l,r = 0, len(S)
        result = []
        
        for i in S:
            if(i=='I'):
                result.append(l)
                l += 1
            else:
                result.append(r)
                r -= 1
        return result+[l]
