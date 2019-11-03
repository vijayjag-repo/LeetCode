class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        
        Approach:
        
        Tarjans - LeetCode Discussion
        """
        graph = [[] for _ in range(n)]
        
        for (x,y) in connections:
            graph[x].append(y)
            graph[y].append(x)
        
        N = len(connections)
        lev = [None] * N
        low = [None] * N
        
        def dfs(node,parent,level):
            if lev[node] is not None:
                return
            lev[node] = low[node] = level
            for nei in graph[node]:
                if not lev[nei]:
                    dfs(nei,node,level+1)
            cur = min([level]+[low[nei] for nei in graph[node] if nei!=parent])
            low[node] = cur
        
        dfs(0,None,0)
        ans = []
        
        for (u,v) in connections:
            if low[u]>lev[v] or low[v]>lev[u]:
                ans.append([u,v])
        return ans
              
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        
        TLE for 4 testcases
        """
        graph = [[] for _ in range(n)]
        ans = []
        
        for (x,y) in connections:
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(i):
            if visited[i]==1:
                return
            else:
                visited[i] = 1
                for j in graph[i]:
                    dfs(j)
        
        for (u,v) in connections:
            visited = [0 for _ in range(n)]
            count = 0
            graph[u].remove(v)
            graph[v].remove(u)
            for i in range(n):
                if visited[i]==0:
                    dfs(i)
                    count+=1
                
            if(count>1):
                ans.append([u,v])
            graph[u].append(v)
            graph[v].append(u)
        
        return ans
                
                
