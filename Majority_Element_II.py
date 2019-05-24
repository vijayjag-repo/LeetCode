class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = dict()
        min_val = len(nums)/3
        ans = []
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]] = 1
        
        for i in d:
            if(d[i]>min_val):
                ans.append(i)
        
        return(ans)
        
        
        
