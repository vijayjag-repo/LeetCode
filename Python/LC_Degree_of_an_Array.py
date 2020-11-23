class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
    
        """
        left, right, count = {},{},{}
        
        for i,val in enumerate(nums):
            if val not in left:
                left[val] = i
            right[val] = i
            count[val] = count.get(val,0) + 1
        
        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if(count[x]==degree):
                ans = min(ans,right[x]-left[x]+1)
        
        return(ans)
            
