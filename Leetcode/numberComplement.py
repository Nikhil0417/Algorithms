class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = bin(num)
        #print(a)
        b = "0b"
        for i in a[2:]:
            x = int(i)^1
            b += str(x)
        return int(b,2)
