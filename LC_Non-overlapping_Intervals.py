class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        
        Approach:
        
        You need to understand that "The first one to end, leaves the most room for the rest".
        So you sort the intervals based on the ending time. 
        And then you start comparing if the start time of an interval is greater than the ending time of earliest ending interval.
        If yes, you keep doing this process.
        If not, then you need to remove an interval, so you add +1.
        
        """
        if not intervals:
            return(0)
        
        intervals.sort(key = lambda x:x[1])
        end = float('-inf')
        overlap = 0
        
        for i in range(len(intervals)):
            if(intervals[i][0]>=end):
                end = max(intervals[i][1],end)
            else:
                overlap+=1
        return(overlap)
