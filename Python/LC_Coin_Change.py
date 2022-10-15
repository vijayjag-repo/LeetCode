
# Recursive approach with memoizatiojn
from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)
        def dfs(val):
            if val < 0:
                return -1
            if val == 0:
                return 0

            min_cost = float('inf')
            for coin in coins:
                res = dfs(val - coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)

            return min_cost if min_cost != float('inf') else -1

        return dfs(amount)

# DP approach we compute the min coins for each amount
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * (amount)

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], dp[amt-coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
