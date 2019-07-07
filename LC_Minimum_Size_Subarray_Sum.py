class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        
        Sliding Window. Keep adding elements. As soon as you hit the value s, remove element from left and check for sum>=s.
        While condition exists, keep removing from left.
        Finally return result which is the minimum size subarray.
        """
        total = left = 0
        result = float('inf')
        for right, val in enumerate(nums):
            total+=val
            while(total >= s):
                result = min(result, right-left+1)
                total -= nums[left]
                left += 1
        
        return(result if result<=len(nums) else 0)
