class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        d = dict()
        
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]] = 1
        
        for i in d:
            if(d[i]==2):
                ans.append(i)
        
        return(ans)
        
