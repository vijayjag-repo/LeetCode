class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = dict()
        d[0] = 1
        d[1] = 1
        for i in range(2,n+1):
            d[i] = d[i-1] + d[i-2]
            
        return(d[n])
            
