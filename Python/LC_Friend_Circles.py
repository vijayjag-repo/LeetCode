class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        
        Approach:
        
        Simple DFS.
        At each index, call dfs. Which will trigger multiple dfs calls if there's a friend.
        Maintain a seen set for each new index/friend that you see/in contact with.
        Once the original dfs call for a particular index ends, add +1 to ans. We've found the first group.
        
        Now, if all friends are present in the seen set after this first dfs call, then there's just one group and all are 
        mutual friends. Else, you continue the dfs calls for the remaining people as well.
        """
        if not M:
            return(0)
        n = len(M)
        seen = set()
        ans = 0
        
        def dfs(i):
            for (x,y) in enumerate(M[i]):
                if(y) and x not in seen:
                    seen.add(x)
                    dfs(x)
        
        for i in range(n):
            if(i not in seen):
                dfs(i)
                ans+=1
        return(ans)
