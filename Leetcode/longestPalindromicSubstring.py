class Solution:
    def helper(self,s,l,r):
        while(l>=0 and r<=len(s)-1 and s[l]==s[r]):
            l -= 1
            r += 1
        return s[l+1:r]
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            tmp = self.helper(s,i,i)
            if(len(tmp)>len(result)):
                result = tmp
            tmp = self.helper(s,i,i+1)
            if(len(tmp)>len(result)):
                result = tmp
        return result
