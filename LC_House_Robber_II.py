class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Approach:
        
        Similar to House Robber.
        """
        if(len(nums)==1):
            return(nums[0])
        
        a = len(nums)
        b = len(nums)-1
        
        def helper(odd,even,x,y):
            for i in range(x,y):
                if(i%2==0):
                    even = max(even+nums[i],odd)
                else:
                    odd = max(odd+nums[i],even)
            return(max(odd,even))
        
        val1 = helper(0,0,0,b)
        val2 = helper(0,0,1,a)
        return(max(val1,val2))
