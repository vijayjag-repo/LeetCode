import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        
        Approach:
        
        Simple Heap implementation.
        """
        pq = [-x for x in stones]
        heapq.heapify(pq)
        
        for i in range(len(stones)-1):  
            x,y = -heapq.heappop(pq),-heapq.heappop(pq)
            heapq.heappush(pq,-abs(x-y))
        
        return(-pq[-1])
