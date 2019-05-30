class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        We know that the input array is sorted and that we do not need to remove the duplicate elements.
        So, we need to have the unique elements from index 0,1,2... and so on.
        So, we initialize a variable x = 1, because, that should be the position of the next unique element.
        Similarly, 2 will be the position of the next unique element.
        So, whenever we encounter a new element, we just copy it to its respective index(to-be) and return the length.
        """
        x = 1
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[x] = nums[i+1]
                x+=1
        
        return(x)
            
        
        
