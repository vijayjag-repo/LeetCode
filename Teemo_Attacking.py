class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        Approach:
        If the next time point is greater than the current time point plus the duration, then,
                        we simply have to add the duration at each time point.
        If the next time point is lesses than the current time point plus the duration, 
                        we just have to add the difference between both the time points.
        Finally, we just add the duration to account for the last time point 
        
        """
        if not timeSeries:
            return(0)
        ans = 0
        for i in range(len(timeSeries)-1):
            if(timeSeries[i]+duration<=timeSeries[i+1]):
                ans+= duration
            else:
                ans+= timeSeries[i+1]-timeSeries[i]
        ans+=duration
        return(ans)
        
            
        
