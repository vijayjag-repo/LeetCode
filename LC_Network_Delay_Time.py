from collections import defaultdict,deque
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        q = [(0,K)]
        d = dict()
        
        for (u,v,t) in times:
            graph[u].append((v,t))
    
        while(q):
            time,node = heapq.heappop(q)
            if node not in d:
                d[node] = time
                for city,travel_time in graph[node]:
                    heapq.heappush(q,(time+travel_time,city))
        
        return(max(d.values()) if len(d)==N else -1)
        
                
# BFS Deque
from collections import defaultdict,deque
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        q = deque([(0,K)])
        d = [0]+[float('inf')]*N
    
        for (u,v,t) in times:
            graph[u].append((v,t))
    
        while(q):
            time,node = q.popleft()
            if(time<d[node]):
                d[node] = time
                for city,travel_time in graph[node]:
                    q.append((time+travel_time,city))

        return(max(d) if max(d)<float('inf') else -1)
        
                
        
