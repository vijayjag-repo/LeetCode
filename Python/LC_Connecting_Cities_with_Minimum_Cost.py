class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        Approach:
        
        1) First, sort based on cost.
        2) If two cities are not in the same set, you need to union them.
        3) While union-ing them, you give the second city's value to the first one.(c1 will take the value of c2)
        4) If they both are in the same set, you do nothing because it does not contribute
        5) Finally, all cities should be in the same set. And each city points to the same leader(This should be 1).
        """
        if len(connections)<N-1:
            return(-1)
        if(N==1):
            return(0)
        
        uf = {}
        def find(c):
            uf.setdefault(c,c)
            if(uf[c]!=c):
                uf[c] = find(uf[c])
            return(uf[c])
        
        def union(c1,c2):
            uf[find(c1)] = find(c2)
        
        ans = 0
        for (c1,c2,cost) in sorted(connections,key = lambda x:x[2]):
            if(find(c1)!=find(c2)):
                union(c1,c2)
                ans+=cost
        
        return(ans if len({find(c) for c in uf}) else -1)
        
        
