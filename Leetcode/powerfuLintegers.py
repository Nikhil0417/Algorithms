class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        num = set()
        for i in range(0,100):
            for j in range(0,100):
                a = x**i+y**j
                if(a<=bound):
                    num.add(a)
                else:
                    break
        return list(num)
