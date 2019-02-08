from collections import defaultdict
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        #print(d)
        
        for i in range(len(s)):
            if(d[s[i]]==1):
                return i
        return -1
