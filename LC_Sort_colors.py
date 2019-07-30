# O(n) and O(1) space solution
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        white = red = 0
        blue = len(nums)-1
        
        while(white<=blue):
            if(nums[white]==0):
                nums[white],nums[red] = nums[red],nums[white]
                white+=1
                red+=1
            elif(nums[white]==1):
                white+=1
            else:
                nums[white],nums[blue] = nums[blue],nums[white]
                blue-=1
                
# naive approach: just count the red,white,blue and overwrite 

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
            
            
