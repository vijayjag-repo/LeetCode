class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        
        Approach:
        
        Assign a color for the node and then call dfs on it.
        If the neighbor has a different color, then no problem. If it has the same color, return False
        If the neighbor has no color, assign a different color and continue the same process.
        
        """
        color = dict()
        def dfs(node):
            for nei in graph[node]:
                if nei in color:
                    if(color[nei]==color[node]):
                        return False
                else:
                    color[nei] = 1-color[node]
                    if not dfs(nei):
                        return False
            return True
        
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
                
        return True
