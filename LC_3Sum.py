class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums)<3):
            return([])
        nums.sort()
        final = set()
        sums = 0
        
        for index,val in enumerate(nums):
            i,j = index +1, len(nums)-1
            while(i<j):
                sums = val + nums[i] + nums[j]
                if(sums==0):
                    final.add((val,nums[i],nums[j]))
                    if(nums[i]==nums[j]):
                        break
                    i+=1
                    j-=1
                elif(sums>0):
                    if(nums[i]==nums[j]):
                        break
                    j-=1
                elif(sums<0):
                    if(nums[i]==nums[j]):
                        break
                    i+=1
        
        return(list(final))
            
        
