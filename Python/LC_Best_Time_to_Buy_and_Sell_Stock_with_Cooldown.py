class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return(0)
        buy = 0
        sell = -prices[0]
        cd = 0
        
        for i in range(1,len(prices)):
            prev_cd = cd
            cd = sell + prices[i]
            sell = max(buy-prices[i],sell)
            buy = max(buy,prev_cd)
        
        return(max(buy,cd))
