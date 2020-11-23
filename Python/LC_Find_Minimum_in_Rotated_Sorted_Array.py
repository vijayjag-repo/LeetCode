class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Approach:
        1) If len(nums)==1, return the only element
        2) If the last element in the array is greater the first element, then the array is sorted entirely(no rotation)
            => Return nums[0]
        3) If nums[mid]>nums[mid+1], we've found the inflection point and therefore, return nums[mid+1].
        4) If nums[mid-1]>nums[mid], we've found the inflection point and therefore, return nums[mid].
        5) If nums[mid]>nums[0], it means that the array is increasing till now and the inflection point is beyond mid.
           Therefore, we change our low = mid + 1.
        6) If nums[mid]<nums[0], it means that the inflection point is somewhere before mid.
           Therefore, we change our high = mid - 1.
        """
        if(len(nums)==1):
            return(nums[0])
        low = 0
        high = len(nums)-1
        target = nums[0]
        if(nums[high]>target):
            return(target)
        
        while(low<high):
            mid = (low+high)/2
            if(nums[mid]>nums[mid+1]):
                return(nums[mid+1])
            if(nums[mid-1]>nums[mid]):
                return(nums[mid])
            
            if(nums[mid]>target):
                low = mid + 1
            else:
                high = mid - 1
