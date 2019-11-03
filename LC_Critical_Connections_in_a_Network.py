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
                
                
