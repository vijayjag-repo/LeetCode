class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Using a hashmap we can do it in O(n) time.
        """
        if(len(nums)==1):
            return(False)
        new = {}
        for i in range(len(nums)):
            if(nums[i] in new):
                return(new[nums[i]],i)
            else:
                new[target-nums[i]] = i
        
