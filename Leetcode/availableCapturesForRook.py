class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        lCount = 0
        rCount = 0
        uCount = 0
        dCount = 0
        for i in range(len(board)):
            if('R' in board[i]):
                y = board[i].index('R')
                x = i
        a = x
        b = y
        # print(x,y)
        # print(board[x][y])
        while(x<8):
            #print(board[x][y])
            if(board[x][y]=='p'):
                dCount += 1
                break
            if(board[x][y]=='B'):
                break
            x += 1
        
        x = a
        while(x>0):
            if(board[x][y]=='p'):
                uCount += 1
                break
            elif(board[x][y]=='B'):
                break
            x -= 1
        x = a
        while(y>0):
            if(board[x][y]=='p'):
                rCount += 1
                break
            elif(board[x][y]=='B'):
                break
            y -= 1
        y = b
        while(y<8):
            #print(board[x][y])
            if(board[x][y]=='p'):
                lCount += 1
                break
            elif(board[x][y]=='B'):
                break
            y += 1
        #print(lCount,rCount,uCount,dCount)
        return (lCount+rCount+uCount+dCount)
