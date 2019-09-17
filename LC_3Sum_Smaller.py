class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        Approach:
        
        This is the same class 3sum but if we've found that a certain combination yields a sum less than target,
        any combination within that range is bound to be less than the target(since we've sorted the array).
        This is done using count+=r-l, where you count the different possibilities that r or l can take with one of them contstant.
        """
        nums.sort()
        count = 0
        sums = 0
        
        for i,val in enumerate(nums):
            l,r = i+1,len(nums)-1
            while(l<r):
                sums = val + nums[l] + nums[r]
                if(sums<target):
                    count+=r-l
                    l+=1
                else:
                    r-=1
        
        return(count)
