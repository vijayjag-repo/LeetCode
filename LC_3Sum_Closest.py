class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(len(nums)<3):
            return([])
        nums.sort()
        final = nums[0] + nums[1] + nums[2]
        for index,val in enumerate(nums):
            i,j = index+1,len(nums)-1
            while(i<j):
                sums = val + nums[i] + nums[j]
                if(sums==target):
                    return(sums)
                elif(abs(target-sums)<abs(target-final)):
                    final = sums
                elif(sums>target):
                    j-=1
                elif(sums<target):
                    i+=1
        return(final)
        
