# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        Approach:
          First, sort the intervals
          Second, push the ending time of the first interval into the heap
          If the starting time of the current interval is greater than the ending time of the interval in the heap,
          then, both the meetings can be attended. Now, remove the previous interval and replace it with the current interval
          If the starting time of the current interval is lesser than the ending time of the interval in the heap,
          then, return False
        """
        if not intervals:
            return(True)
        free = []
        intervals.sort(key = lambda x : x.start)
        heapq.heappush(free,intervals[0].end)
        
        for i in intervals[1:]:
            if(free[0]<=i.start):
                heapq.heappop(free)
                heapq.heappush(free,i.end)
            else:
                return(False)
        return(True)
           
# Normal Sort and compare
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return(True)
        intervals.sort()
        for i in range(1,len(intervals)):
            if(intervals[i][0]<intervals[i-1][1]):
                return(False)
        return(True)
