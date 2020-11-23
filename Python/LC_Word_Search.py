class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        
        Approach:
        DFS. For every single letter that you see, you explore the neighbours.
        in dfs(), result line can also be modified to,
        
        result = False
        for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
            result = result or self.dfs(board,word[1:],row+x,col+y)
        
        Just for the sake of clarity.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(self.dfs(board,word,i,j)):
                    return(True)
        return(False)
    
    def dfs(self,board,word,row,col):
        if(len(word)==0):
            return(True)
        
        if(row<0 or row>=len(board) or col<0 or col>=len(board[0]) or board[row][col]!=word[0]):
            return(False)
        
        temp = board[row][col]
        board[row][col] = '@'
        
        result = self.dfs(board,word[1:],row+1,col) or self.dfs(board,word[1:],row-1,col) or self.dfs(board,word[1:],row,col+1) or self.dfs(board,word[1:],row,col-1)
        
        board[row][col] = temp
        return(result)
        
