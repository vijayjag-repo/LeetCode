class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        Approach:
        
        DFS based.
        """
        visited = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]
        
        for (x,y) in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(i,graph,visited):
            if visited[i]==1:
                return
            visited[i] = 1
            for j in graph[i]:
                dfs(j,graph,visited)
                
        ans = 0
        for i in range(n):
            if visited[i]==0:
                dfs(i,graph,visited)
                ans+=1
                
        return ans
        
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        
        Approach:
        
        Union find by rank.
        """
        parent = range(n)
        rank = [0] * n
        def find(x):
            return parent[x] if parent[x]==x else find(parent[x])
            
        for e in edges:
            x, y = map(find, e)
            if rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1
        
        return len({find(x) for x in parent})
     


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        
        Approach:
        
        Same as connecting connections.
        Key idea: Do union find using ranking and return the number of sets present.
        """
        if n==1:
            return(1)
        
        uf = {}
        rank = [0]*(n)
        
        def find(e):
            uf.setdefault(e,e)
            if(uf[e]!=e):
                uf[e] = find(uf[e])
            return(uf[e])
        
        def union(e1,e2):
            if(rank[e1]<rank[e2]):
                uf[find(e1)] = find(e2)
            elif(rank[e2]<rank[e1]):
                uf[find(e2)] = find(e1)
            else:
                uf[find(e2)] = find(e1)
                rank[e1]+=1
            
        for e1,e2 in sorted(edges,key = lambda x:x[0]):
            if(find(e1)!=find(e2)):
                union(e1,e2)
                
        return(len({find(c) for c in uf})+n-len(uf))
