class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        count = 0
        while(Y>X):
            if(Y%2==1):
                count += 1
                Y += 1
            else:
                count += 1
                Y /= 2
        return int(count+(X-Y))
