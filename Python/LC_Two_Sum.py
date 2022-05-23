class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        #1 - https://leetcode.com/problems/two-sum/
        
        Naive Approach
        -----
        
        * Have couple of loops
            * For each element in the outer loop, add element in the inner loop and check if that equals target
            * Return corresponding indexes if the numbers add up
        
        Time complexity: O(n^2)
        Space complexity: O(1)
        
        Optimal Approach
        -----
        * Have a dictionary/hashmap initialized 
        * Run a loop 
            * For each (target - element) not found in the dict, add element along with index to the dictionary
            * If (target - element) is found, return corresponding indexes
        
        Time complexity: O(n)
        Space complexity: O(n)
        """
        d = dict()
        
        for i in range(len(nums)):
            if (target - nums[i] in d):
                return [d[target-nums[i]], i]
            else:
                d[nums[i]] = i
        
