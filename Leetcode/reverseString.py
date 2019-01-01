class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = []
        p = []
        str = ""
        x = len(s)
        for i in s:
            a.append(i)
        for i in range(0,x):
            #print(a[i])
            #print(a[x-i-1])
            p.append(a[x-i-1])
            str = str + p[i]
        #print(str)
        return str
