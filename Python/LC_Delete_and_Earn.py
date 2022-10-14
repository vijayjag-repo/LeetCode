
# DP - Reducing to house robber question
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.Counter(nums)
        dp = [0] * (max(nums) + 1)
        for key in d:
            dp[key] = key * d[key]

        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i] + dp[i-2])

        return dp[-1]


# Same DP approach but without using the extra dp array

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        points, prev, curr = collections.Counter(nums), 0, 0

        for value in range(max(points.keys()) + 1):
            prev, curr = curr, max(prev + value * points[value], curr)
        return curr

    
