class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        
        Approach:
        
        Straightforward.
        Alternatively, you can also pass destination, start to the calling function incase destination is smaller than start.
        """
        if not distance or start==destination:
            return(0)
        
        ans1 = 0
        ans2 = 0
        if(start<destination):
            ans1 = sum(distance[start:destination])
            ans2 = sum(distance[:start]+distance[destination:])
        else:
            ans1 = sum(distance[destination:start])
            ans2 = sum(distance[:destination]+distance[start:])
        return(min(ans1,ans2))
