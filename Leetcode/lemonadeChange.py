class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        for i in bills:
            if(i==5):
                five += 1
            elif(i==10):
                five -= 1
                ten += 1
            else:
                five -= 1
                ten -= 1
                if(ten<0):
                    five -= 2
                    ten = 0
            if(five<0):
                return False
        return True
