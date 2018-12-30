class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        fin = []
        for i in s.lower():
            if i.isalnum():
                print(i)
                fin.append(i)
        #print(fin)
        return fin==fin[::-1]
