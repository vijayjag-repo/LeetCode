class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        cur_end = 0
        cur_farthest = 0
        for i in range(len(nums)-1):
            cur_farthest = max(cur_farthest,nums[i]+i)
            if(i==cur_end):
                jumps+=1
                cur_end = cur_farthest
        
        return(jumps)
        
        
