class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = []
        count = 0
        for i in range(len(nums)):
            if(nums[i]==1):
                count+=1
            else:
                new.append(count)
                count = 0
        new.append(count)
        return(max(new))
        
        
        
