class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = collections.Counter(nums)
        zero = count[0]
        one = count[1]
        two = count[2]
        for i in range(len(nums)):
            if(zero>0):
                nums[i] = 0
                zero-= 1
            else:
                if(one>0):
                    nums[i] = 1
                    one-= 1
                else:
                    if(two>0):
                        nums[i] = 2
                        two-= 1
        
        
        
                
        
            
