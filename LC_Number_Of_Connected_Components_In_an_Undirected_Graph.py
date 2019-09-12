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
