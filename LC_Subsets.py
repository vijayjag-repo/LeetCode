class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Approach:
        
        At every index you have a decision to make. Consider [1,2,3]
        At index 0, you have the choice of either choosing 1 or leaving 1.
        At index 1, you have the choice of either choosing 2 or leaving 2.
        And so on.
        
        """
        final = []
        
        def helper(nums,index,path,final):
            final.append(path)
            for i in range(index,len(nums)):
                helper(nums,i+1,path+[nums[i]],final)
        
        helper(nums,0,[],final)
        return(final)
