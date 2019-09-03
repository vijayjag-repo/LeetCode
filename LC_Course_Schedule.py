class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        
        Appproach:
        
        If a node is not visited, set it to 0.(Set all to 0 initially)
        If a node is currently being processed or being explored, set it to -1.
        If a node is currently done exploring, set it to 1.
        
        At any point during the dfs search, if you see a node which is already being explored(seen twice), cycle is present.
        Else,
        explore all neighbors and finally set the node to 1 after exploration.
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        for c,p in prerequisites:
            graph[c].append(p)
    
        def dfs(i):
            if(visited[i]==-1):
                return(False)
            if(visited[i]==1):
                return(True)
            
            visited[i] = -1
            for x in graph[i]:
                if(not dfs(x)):
                    return(False)
            
            visited[i] = 1
            return(True)
        
        for i in range(numCourses):
            if(not dfs(i)):
                return(False)
        return(True)
        
