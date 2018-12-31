class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        nums = []
        se = []
        for i in range(left,right+1):
            if (i%10!=0):
                nums.append(i)
        #print(nums)
        for i in nums:
            s = str(i)
            count = 0
            for j in range(len(s)):
                if(s[j]!='0'):
                    if(i%int(s[j])==0):
                        count += 1
            if(count==len(s)):
                se.append(i)
        return se
