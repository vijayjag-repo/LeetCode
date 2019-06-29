class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        
        Approach:
        
        Simple dp. Just draw the recursion tree. Each point, you can take two decisions, either right or down.
        """
        dp = [[1 for i in range(n)] for j in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return(dp[-1][-1])
                
        
