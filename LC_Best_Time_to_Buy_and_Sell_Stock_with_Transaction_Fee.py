
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
      
        Idea:
        
        If I am holding a share after today, then either I am just continuing holding the share I had yesterday, 
        or that I held no share yesterday, but bought in one share today: hold = max(hold, cash - prices[i])
        If I am not holding a share after today, then either I did not hold a share yesterday, 
        or that I held a share yesterday but I decided to sell it out today: cash = max(cash, hold + prices[i] - fee).
        Make sure fee is only incurred once.
        """
        cash = 0
        hold = -prices[0]
        
        for i in range(1,len(prices)):
            cash = max(cash,hold+prices[i]-fee)
            hold = max(hold,cash-prices[i])
        
        return(cash)
