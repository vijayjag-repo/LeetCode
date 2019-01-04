class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        count = collections.Counter(nums)
        for i,value in enumerate(nums):
            if(count[value]>length/2):
                return(value)
        
