class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #print(matrix[4][0])
        if(matrix == [] or matrix == [[]]):
            return False
        i = 0
        j = len(matrix[0])-1
        while(i<len(matrix) and j>=0):
            if(matrix[i][j]>target):
                j -= 1
            elif(matrix[i][j]< target):
                i += 1
            else:
                return True
        return False
