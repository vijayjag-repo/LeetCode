class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_current = max_global = nums[0]
        if not nums:
            return(0)
        else:
            for i in range(1,len(nums)):
                max_current = max(nums[i],max_current+nums[i])
                max_global = max(max_current,max_global)
            return(max_global)
        
        
        
