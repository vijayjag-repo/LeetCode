class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        odd = 0
        
        for i in range(len(nums)):
            if(i%2==0):
                even = max(even + nums[i],odd)
            else:
                odd = max(odd + nums[i],even)
        return(max(even,odd))
