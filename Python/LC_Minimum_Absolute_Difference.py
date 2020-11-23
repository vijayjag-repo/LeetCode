import collections
from collections import defaultdict
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        if not arr:
            return []
        
        arr.sort()
        d = defaultdict(list)
        for i in range(len(arr)-1):
            d[abs(arr[i+1] - arr[i])].append([arr[i],arr[i+1]])
            
        min_val = min(d.keys())
        return d[min_val]
      
