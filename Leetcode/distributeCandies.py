class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        dist = len(set(candies))
        sisCandies = len(candies)/2
        if(dist>=sisCandies):
            return sisCandies
        else:
            return dist
