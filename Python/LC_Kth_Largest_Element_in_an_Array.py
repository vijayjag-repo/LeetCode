class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """ 
        # Solution 1
        # There are different variations which you can do with heap. This is one of the smallest along with heapq.nlargest()
        
        heapq.heapify(nums)
        for i in range(len(nums)-k+1):
            val = heapq.heappop(nums)
        return(val)
            
            
        
