class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split(" ")
        b = ""
        for i in a:
            b += i[::-1]+" "
        #print(b)
        return b[:len(b)-1]
