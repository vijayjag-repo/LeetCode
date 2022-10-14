# DP approaches

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        odd = 0

        for i in range(len(nums)):
            if(i%2==0):
                even = max(even + nums[i],odd)
            else:
                odd = max(odd + nums[i],even)
        return(max(even,odd))
