class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        
        Approach:
        
        You're given click, which corresponds to a particular coordinate within the board.
        If this point is a mine, you change the board to 'X' and return the board.
        Else,
        This point could be an unrevealed square.
        
        The first thing that you do is, check if this point has any mines nearby. 
        If it does not have any mines nearby, you gotta call its neighbors and set the current point to 'B'.
        Else,
        you set the current point to whatever the mine value is and do not call dfs.
        
        Finally after first dfs calls ends, you return the state of the board.
        
        """
        neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        def dfs(x,y):
            mine = 0
            for (i,j) in neighbors:
                if(0<=x+i<len(board) and 0<=y+j<len(board[0]) and board[x+i][y+j]=='M'):
                    mine+=1
            if(mine>0):
                board[x][y] = str(mine)
            else:
                board[x][y] = 'B'
                for (i,j) in neighbors:
                    if(0<=x+i<len(board) and 0<=y+j<len(board[0]) and board[x+i][y+j]=='E'):
                        dfs(x+i,y+j)
                
        x,y = click
        if(board[x][y]=='M'):
            board[x][y] = 'X'
        else:
            dfs(x,y)
        
        return board
