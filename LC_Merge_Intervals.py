class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        
        Approach:
        
        First, we sort the intervals.
        Assign the first value in intervals to current.
        Iterate through intervals, if the interval's start time is less than the end time of current,
        you can merge them => see which has the maximum end time out of the two. That is the end time of the new interval.
        Else, append the current to the final and set the interval to current.
       
        
        """
        if not intervals:
            return([])
        
        final = []
        intervals.sort()
        curr = intervals[0]
        for i in range(1,len(intervals)):
            if(intervals[i][0]<=curr[1]):
                curr[1] = max(curr[1],intervals[i][1])
            else:
                final.append(curr)
                curr = intervals[i]
        final.append(curr)
        return(final)
