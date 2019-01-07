class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Input: [7,1,5,3,6,4]
        Output: 7
        Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                     Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
        """
        max_profit = 0
        if(len(prices)==0):
            return(0)
        
        for i in range(1,len(prices)):
            if(prices[i] - prices[i-1] > 0):
                max_profit+= prices[i] - prices[i-1]
        
        return(max_profit)
