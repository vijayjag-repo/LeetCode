class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = 0
        right_sum = 0
        for i in nums:
            right_sum+=i
        
        for i,value in enumerate(nums):
            right_sum-=value
            if(left_sum==right_sum):
                return(i)
            else:
                left_sum+=value
        return(-1)
        
            
        
        
