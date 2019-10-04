class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums)<3):
            return []
        nums.sort()
        l = 0
        r = len(nums)-1
        sums = 0
        ans = set()
        
        for index,val in enumerate(nums):
            if index > 0 and nums[index-1] == nums[index]:
                continue
            l,r = index+1,len(nums)-1
            while(l<r):
                sums = val+nums[l]+nums[r]
                if(sums==0):
                    ans.add((val,nums[l],nums[r]))
                    l+=1
                    r-=1
                elif(sums<0):
                    l+=1
                else:
                    r-=1
        return list(ans)
