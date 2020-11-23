class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        neighbors = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
        
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                live = 0
                for neighbor in neighbors:
                    r = (row+neighbor[0])
                    c = (col+neighbor[1])
                    
                    if(r<rows and r>=0) and (c<cols and c>=0) and abs(board[r][c])==1:
                        live+=1
                        
                if(board[row][col]==1) and (live<2 or live>3):
                    board[row][col] = -1
                if(board[row][col]==0) and (live==3):
                    board[row][col] = 2
        
        for row in range(rows):
            for col in range(cols):
                if(board[row][col]>0):
                    board[row][col] = 1
                else:
                    board[row][col] = 0
