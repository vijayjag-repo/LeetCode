class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_current = max_global = 0
        if not prices:
            return(0)
        else:
            for i in range(1,len(prices)):
                max_current = max(0,max_current + prices[i] - prices[i-1])
                max_global = max(max_global,max_current)
            return(max_global)
        
