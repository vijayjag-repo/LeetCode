# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        Approach:
            Sort intervals based on start time
            Push the end time of the first interval into the heap
            If the end time of top of heap is less than start time of the interval, 
            then top of heap is popped and this new interval is pushed into its place 
            Else,
            just push this new interval into the heap
        """
        if not intervals:
            return(0)
        
        free = []
        intervals.sort(key = lambda x : x.start)
        heapq.heappush(free,intervals[0].end)
        
        for i in intervals[1:]:
            if(free[0]<=i.start):
                heapq.heappop(free)
            heapq.heappush(free,i.end)
            
        return(len(free))
    
