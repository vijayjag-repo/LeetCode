# Interesting DP problem;take a piece of paper and work out an example
# Draw a matrix to find out the pattern
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n = len(text1)
        m = len(text2)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return dp[-1][-1]
