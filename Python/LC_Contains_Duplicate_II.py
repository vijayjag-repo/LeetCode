class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = dict()
        for index,value in enumerate(nums):
            if(value in d and abs(d[value]-index)<=k):
                return(True)
            else:
                d[value] = index
        return(False)
            
        
        
