class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Straightforward
        """
        nums.sort()
        maximum = nums[-1]*nums[-2]*nums[-3]
        
        if(nums[0]<0 and nums[1]<0):
            maximum = max(maximum, nums[-1]*nums[0]*nums[1])
        
        return(maximum)
        
                
