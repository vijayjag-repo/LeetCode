class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        Approach:
        
        Draw the tree for each number of nodes. Base case is pretty obvious because you can draw only one tree if you have one node.
        For two nodes, its again obvious. 
        All the other cases involve some combination of the previous cases. Work it out to see.
        
        """
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            for j in range(i):
                dp[i]+= dp[j]*dp[i-j-1]
        
        return(dp[-1])
        
        
