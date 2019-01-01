class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if(nums[0]==0 and len(nums)==1):
            return(1)
        elif(nums[0]==1):
            return(0)
        a = collections.Counter(nums)
        print(a)
        for i,value in enumerate(a):
            if(i!=value):
                return(i)
        return(len(nums))
                
