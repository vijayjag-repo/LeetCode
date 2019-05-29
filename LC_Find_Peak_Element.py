class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==1):
            return(0)
        if(len(nums)==2):
            return(nums.index(max(nums)))
        for i in range(1,len(nums)-1):
            if(nums[i]>nums[i-1] and nums[i]>nums[i+1]):
                return(i)
            else:
                return(nums.index(max(nums)))
        
