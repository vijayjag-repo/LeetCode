class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i]*= product
            product*= nums[i]
        
        product = 1
        for i in range(len(nums)-1,-1,-1):
            output[i]*= product
            product*= nums[i]
        
        return(output)
                
        
            
            
        
