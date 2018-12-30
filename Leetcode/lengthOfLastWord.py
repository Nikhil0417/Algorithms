class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        b = s.strip()
        a = b.split(' ')
        y = len(a)
        #print(a[y-1])
        #print(a[y-2])
        print(y)
        if a[y-1] == "":
            q = len(a[y-2])
            print(q)
            return q
        else:
            x = len(a[y-1])
            print(x)
            return x
        
        
