class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        Approach:
        
        DFS. You want to count the max area out of all the islands. 
        First you start from (0,0) and you keep exploring until you find a '1' which corresponds to a part of an island.
        Now, '1' means that the area is 1. Next, you explore its neighbors to find anymore 1's.
        If more 1's are there, you add them to the result. Then if there are no more 1's as neighbors, you return the result.
        This result is stored as the maximum.
        
        Now, this process keeps on going across the grid. Finally, after all the points have been seen, 
        we know the maximum area out of these. Return them.
        """
        m = len(grid)
        n = len(grid[0])
        max_val = 0
        
        def dfs(i,j):
            if(0<=i<m and 0<=j<n and grid[i][j]):
                grid[i][j] = 0
                return(1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1))
            return(0)
        
        for x in range(m):
            for y in range(n):
                if(grid[x][y]):
                    max_val = max(dfs(x,y),max_val)
        return(max_val)
