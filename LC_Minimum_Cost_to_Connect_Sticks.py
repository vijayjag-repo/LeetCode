import heapq
class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        if not sticks:
            return(0)
        
        heapq.heapify(sticks)
        cost = 0
        while(len(sticks)>1):
            val1 = heapq.heappop(sticks)
            val2 = heapq.heappop(sticks)
            cost+=val1+val2
            heapq.heappush(sticks,val1+val2)
        
        return(cost)
            
            
