class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        Whenever you see a number, you just change the number corresponding to its index as negative.
        Finally, you'll see that some indexes are still left with positive numbers.
        These indexes are our left out numbers.
        
        Also, this approach would work only if the numbers are present sequentially within a specified range.
        """
        for i in range(len(nums)):
            if(nums[abs(nums[i])-1] >0):
                nums[abs(nums[i])-1]*=-1
        
        return([(i+1) for i in range(len(nums)) if nums[i]>0])
        
       
                
        
        
                
            
        
