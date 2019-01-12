# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        
        """
        if(len(intervals)==0):
            return([])
        intervals.sort(key = lambda x : x.start)
        merged = []
        cur = intervals[0]
        for i in range(1,len(intervals)):
            if(intervals[i].start<=cur.end):
                cur.end = max(cur.end, intervals[i].end)
            else:
                merged.append(cur)
                cur = intervals[i]
        merged.append(cur)
        return(merged)
        
