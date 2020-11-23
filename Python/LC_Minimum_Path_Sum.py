class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        Tushar Roy Video.
        Approach:
        
        First, sum up the first row and sum up the first column in grid.
        Then, straight forward dp. add minimum of [i-1][j] and [i][j-1]
        Return the last element in the grid which has the minimum path sum.
        
        """
        m = len(grid)
        n = len(grid[0])
        
        for i in range(1,n):
            grid[0][i]+= grid[0][i-1]
        
        for j in range(1,m):
            grid[j][0]+= grid[j-1][0]
        
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]+= min(grid[i-1][j],grid[i][j-1])
        return(grid[-1][-1])
        
            
        
        
        
        
        
        
