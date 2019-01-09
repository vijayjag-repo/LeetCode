class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        new = collections.Counter(nums)
        value = zip(*new.most_common(k))
        return(value[0])
        

        
