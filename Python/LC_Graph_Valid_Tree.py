class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        
        Approach:
        
        Basic idea is that, initially all the nodes are mapped to each other.
        As and when you see an edge, you assign the second vertice in the edge to be the parent of the first vertice.
        
        Example [0,1],[1,2]. Here 0 is mapped to 1 and is mapped to 2.
        If you add a new edge [0,2], you check for 0's mapping. 
        First you check is 0 is mapped to itself. If not, you see its parent's mapping.
        So 0 is mapped to 1, 1 is mapped to 2. You compare this with the current vertice 2, whose parent is 2 itself.
        When 2==2, you return False as you've seen a cycle. Draw this to visualize.
        
        Also, you need to check if the number of edges==n-1 which is one of the main properties of connected graphs.
        """
        
        parent = range(n)
        
        def find(x):
            return(x if parent[x]==x else find(parent[x]))
        
        for e in edges:
            x,y = map(find,e)
            if(x==y):
                return(False)
            parent[x] = y
        
        return(len(edges)==n-1)
        
    
        
