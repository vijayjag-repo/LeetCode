class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = collections.Counter(nums)
        zero = count[0]
        one = zero + count[1]
        two = one + count[2]
        i = 0
        while(i<len(nums)):
            if(i<zero):
                nums[i] = 0
                i+=1
            elif(i<one):
                nums[i] = 1
                i+=1
            elif(i<two):
                nums[i] = 2
                i+=1
               
        return(nums)
            
            
