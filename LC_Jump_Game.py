class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]+i>=last):
                last = i
        
        return(last==0)
        
