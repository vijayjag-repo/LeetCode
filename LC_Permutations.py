class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        first = 0
        n = len(nums)
        output = []
        
        def backtrack(first):
            if(first==n):
                output.append(nums[:])
            
            for i in range(first,n):
                nums[first],nums[i] = nums[i],nums[first]
                backtrack(first+1)
                nums[first],nums[i] = nums[i],nums[first]
        
        backtrack(first)
        return(output)
