class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        O(nlogn) approach.
        """
        if not nums:
            return(0)
        nums.sort()
        
        longest = 1
        current = 1
        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1]):
                if(nums[i]==nums[i-1]+1):
                    current+=1
                else:
                    longest = max(longest,current)
                    current = 1
        return(max(longest,current))
