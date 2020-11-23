from collections import defaultdict, deque
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        
        Approach:
        
        Have a graph and deque.
        Each time you pop some node from queue, check if its the destination.
        If its the destination, update the minimum possible price to the destination.
        Else,
        keep adding to the queue while updating the stops and the prices.
        """
        graph = defaultdict(list)
        q = deque()
        min_price = float('inf')
        
        for (u,v,w) in flights:
            graph[u].append((v,w))
        
        q.append((src,0,0))
        while(q):
            city,stops,price = q.popleft()
            if(city==dst):
                min_price = min(min_price,price)
                continue
            
            if(stops<=K and price<=min_price):
                for nei,price_nei in graph[city]:
                    q.append((nei,stops+1,price+price_nei))
        
        return(min_price if min_price!=float('inf') else -1)
