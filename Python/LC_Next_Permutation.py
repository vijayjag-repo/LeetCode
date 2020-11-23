class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        
        Approach:
        See Back to Back SWE video from explanation.
        """
        
        i = j = len(nums)-1
        
        while(i > 0 and nums[i-1]>=nums[i]):
            i-= 1
        if(i==0): 
            # nums are in descending order
            nums.reverse()
            return 
        
        #find the ascending position from last
        k = i-1    
        while nums[j] <= nums[k]:
            j-= 1
        #swap that element
        nums[k], nums[j] = nums[j], nums[k]  
        
        
        l, r = k+1, len(nums)-1  
        # reverse the second part
        while(l < r):
            nums[l], nums[r] = nums[r], nums[l]
            l+=1 
            r-= 1
        
