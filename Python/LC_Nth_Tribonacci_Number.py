class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        y = 1
        z = 1

        if n < 3:
            return y if n > 0 else x

        for i in range(3, n+1):
            ans = x + y + z
            x, y, z = y, z, ans

        return ans

# Classic DP approach

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = dict()
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]
