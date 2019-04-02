class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = collections.Counter(nums)
        for i in range(0,count[0]):
            nums.remove(0)
            nums.append(0)
        
        
