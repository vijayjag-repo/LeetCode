class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        
        Approach:
        
        Similar to subarray sum but you've to maintain the length of the largest subarray sum.
        """
        maximum = 0
        sums = 0
        d = dict()
        d[0] = -1
        
        for i in range(len(nums)):
            sums+=nums[i]
            if(sums-k in d):
                maximum = max(maximum,i-d.get(sums-k))
            if(sums not in d):
                d[sums] = d.get(sums,i)
        
        return(maximum)
