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

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = dict()
        stack = [nums[::-1]
        ans = [-1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(nums[i])
        return ans
