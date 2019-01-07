class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        initial = [0,0]
        for i in range(len(moves)):
            if(moves[i]=='U'): 
                initial[1] += 1
            elif(moves[i]=='D'):
                initial[1] -= 1
            elif(moves[i]=='R'):
                initial[0] += 1
            elif(moves[i]=='L'):
                initial[0] -= 1
            else:
                pass
        if(initial==[0,0]):
            return True
        else:
            return False
