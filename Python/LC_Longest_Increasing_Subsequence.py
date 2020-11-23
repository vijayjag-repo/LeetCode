class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Tushar Roy video.
        nums = [some numbers]
        dp = [1,1,.....1,1]
        If nums[j]<nums[i]:
            dp[i] = max(dp[i],dp[j])
        
        Instead of doing this directly, we do the following.
        
        """
        if(len(nums)==0):
            return(0)
        
        dp = [0 for i in range(len(nums))]
        dp[0] = 1
        for i in range(1,len(nums)):
            maxval = 0
            for j in range(i):
                if(nums[j]<nums[i]):
                    maxval = max(maxval,dp[j])
            dp[i] = maxval + 1
            
        return(max(dp))
                
        
