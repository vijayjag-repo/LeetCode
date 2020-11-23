class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        
        Approach:
        
        increment and decrement count/score accordingly. Only the town judge will have a positive score of N-1. 
        """
        trusted = [0]*(N+1)
        
        for (x,y) in trust:
            trusted[x]-=1
            trusted[y]+=1
        
        for i in range(1,N+1):
            if(trusted[i]==N-1):
                return(i)
            
        return(-1)
        
# Approach Two: Exhaustive use of space. Pretty bad
from collections import defaultdict
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust:
            return(1)
        
        d = collections.defaultdict(list)
        seen = set()
        for (x,y) in trust:
            d[y].append(x)
            seen.add(x)
        
        for judge in d:
            if(len(d[judge])==N-1 and judge not in seen):
                return(judge)
        return(-1)
