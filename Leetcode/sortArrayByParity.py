class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        new_list=[]
        for number in A:
            if number%2==0:
                new_list.append(number)
        for number in A:
            if number not in new_list:
                new_list.append(number)
        
        return new_list
