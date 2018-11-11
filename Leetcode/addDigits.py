class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """        
        while(len(str(num)) != 1):
            a = str(num)
            b = 0
            for i in range(0,len(a)):
                b += int(a[i])
            if(len(str(b)) != 0):
                num = b
        return num
    
    #         if len(str(num)) == 1:
#             return 1
#         else:
#             a = num%10
#             b = num/10
#             c = a+b
#             return self.addDigits(c)
