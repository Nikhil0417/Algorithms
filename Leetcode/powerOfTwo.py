def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>1:
            #print(n)
            n = n/2
        if n==1:
            return True
        else:
            #n = n/2
            #self.isPowerOfTwo(n/2)
            return False
# Given an integer, write a function to determine if it is a power of two.
