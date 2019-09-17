class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        sums = 0
        close = float('inf')
        ans = 0
        
        for i,val in enumerate(nums):
            l,r = i+1,len(nums)-1
            while(l<r):
                sums = val + nums[l] + nums[r]
                if(sums==target):
                    return(sums)
                elif(sums<target):
                    l+=1 
                else:
                    r-=1
                    
                if(abs(sums-target)<close):
                    close = abs(sums-target)
                    ans = sums
        return(ans)
                    
