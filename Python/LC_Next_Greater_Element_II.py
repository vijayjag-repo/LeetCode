class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        Approach:
        
        Same as Next greater element 1 but we iterate twice.
        """
        stack = []
        ans = [-1]*len(nums)
        
        for i in range(len(nums))*2:
            while(stack and nums[i]>nums[stack[-1]]):
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return(ans)
        
        
        
