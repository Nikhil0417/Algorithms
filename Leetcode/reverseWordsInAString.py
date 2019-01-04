class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split(" ")
        b = " ".join(list(filter(lambda x: x.strip() ,a[::-1])))
        return b
