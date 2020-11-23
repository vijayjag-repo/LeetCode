class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        Approach:
        
        Beautiful
        """
        if not obstacleGrid:
            return
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if(obstacleGrid[0][0]==1):
            return(0)
        
        obstacleGrid[0][0] = 1
        
        for i in range(1,m):
            obstacleGrid[i][0] = obstacleGrid[i-1][0]*(1-obstacleGrid[i][0])
        for i in range(1,n):
            obstacleGrid[0][i] = obstacleGrid[0][i-1]*(1-obstacleGrid[0][i])
        for i in range(1,m):
            for j in range(1,n):
                obstacleGrid[i][j] = (obstacleGrid[i-1][j]+obstacleGrid[i][j-1])*(1-obstacleGrid[i][j])
        
        return(obstacleGrid[-1][-1])
                    
                
            
            
