class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(0)
        
        current_max = current_min = result = nums[0]
        for i in range(1,len(nums)):
            temp = current_max
            current_max = max(nums[i],current_max*nums[i],current_min*nums[i])
            current_min = min(nums[i],temp*nums[i],current_min*nums[i])
            result = max(result,current_max)
        
        return(result)
            
        
