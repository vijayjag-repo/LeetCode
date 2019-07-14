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
        
        """
        O(n) approach. Simple idea. work with an example.
        """
        
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
