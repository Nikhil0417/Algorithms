class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        maximum=0
        while(i<j):
            maximum = max(maximum,(j-i)*min(height[i],height[j]))
            if(height[i]<height[j]):
                i += 1
            elif(height[i]>=height[j]):
                j -= 1
        return maximum
