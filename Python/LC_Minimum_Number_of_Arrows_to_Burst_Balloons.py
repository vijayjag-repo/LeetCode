class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        
        Approach:
        
        Same as Non-overlapping intervals.
        Sort by ending time.
        If an interval's starting time is less than or equal to the ending time of the earliest ending interval,
        then, they can be grouped.
        Else,
        The current interval cannot be part of the group. 
        """
        if not points:
            return(0)
        
        points.sort(key = lambda x:x[1])
        arrow = 0
        curr = float('-inf')
        
        for interval in points:
            if(interval[0]>curr):
                arrow+=1
                curr = interval[1]
        return(arrow)
