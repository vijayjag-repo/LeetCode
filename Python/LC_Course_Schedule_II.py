class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        if not prerequisites and numCourses:
            return([i for i in range(numCourses)])
        
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        ans = []
        
        for (x,y) in prerequisites:
            graph[x].append(y)
        
        def dfs(i):
            if(visited[i]==-1):
                return(False)
            if(visited[i]==1):
                return(True)
            
            visited[i] = -1
            for j in graph[i]:
                if(not dfs(j)):
                    return(False)
            
            visited[i] = 1
            ans.append(i)
            
            return(True)
            
        for i in range(numCourses):
            if(not dfs(i)):
                return([])
            
        return(ans)
