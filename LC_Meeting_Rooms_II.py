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
        intervals.sort()
        rooms = []
        heapq.heappush(rooms,intervals[0][1])
        for i in range(1,len(intervals)):
            if(rooms[0]<=intervals[i][0]):
                heapq.heappop(rooms)
            heapq.heappush(rooms,intervals[i][1])
        return(len(rooms))
    
