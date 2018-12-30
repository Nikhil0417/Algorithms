class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        length = len(str(x))
        i = x
        rev = 0
        if i > 0:
	        for p in range(1,length+1):
		        y = i%10
		        i = int(i/10)
		        rev = rev + y*(10**(length-p))
        else:
            i = i*(-1)
            for p in range(2,length+1):
                y = i%10
                i = int(i/10)
                rev = rev + y*(10**(length-p))
            rev = rev*(-1)
        if rev > 2147483647 or rev < -2147483647:
            rev = 0
        return rev
    #Challenges faced 1. border-line test cases, 2. 2**32 not working as expected
