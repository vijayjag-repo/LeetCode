class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Solution 1
        new = collections.Counter(nums)
        value = zip(*new.most_common(k))
        return(value[0])
- - - - - - - - - - - -  - - - - - -  - - - - - -
- - - - -  - - - - - - - - - - -- - - - -  - - - 
        # Solution 2
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
        

        
