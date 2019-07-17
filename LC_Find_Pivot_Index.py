class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Approach:
        
        First calculate the right sum.
        Then in the next pass, remove the first element from right sum and add it to left sum. Check for equality.
        Repeat this process.
        
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
        
            
        
        
