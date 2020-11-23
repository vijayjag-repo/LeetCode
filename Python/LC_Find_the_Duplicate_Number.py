class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Approach:
        
        Start with index 0.
        IF the value at index is +ve, change it to -ve and set index = abs(val at current index)
        If the value at index is -ve, return that index.
        
        """
        i = 0
        while(i<len(nums)):
            if(nums[i]>0):
                nums[i]*=-1
                i = abs(nums[i])
            else:
                return(i)
            
        
