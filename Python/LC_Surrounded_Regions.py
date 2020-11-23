class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        
        Approach:
        
        First, go to all the four sides and check if 'O' is present.
        If present, change it to 'D' or any variable and call dfs to search for connected 'O's.
        Once we are done with this, the remaining process is straightforward.
        Change the D's into 'O' and change the 'O's into 'X'.
        
        """
        def dfs(i,j):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!='O':
                return
            else:
                board[i][j] = 'D'
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i in (0,len(board)-1) or j in (0,len(board[0])-1) and board[i][j]=='O':
                    dfs(i,j)
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if(board[x][y]=='D'):
                    board[x][y] = 'O'
                elif(board[x][y]=='O'):
                    board[x][y] = 'X'
        
                    
