# Q5 Spiral Matrix II
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        
        Approach:
        
        Same as Spiral Matrix
        """
        def helper(r1,r2,c1,c2):
            for c in range(c1,c2+1):
                yield(r1,c)
            for r in range(r1+1,r2+1):
                yield(r,c2) 
            if(r2>r1 and c2>c1):
                for c in range(c2-1,c1-1,-1):
                    yield(r2,c)
                for r in range(r2-1,r1,-1):
                    yield(r,c1)
                    
        new = [[1 for _ in range(n)] for _ in range(n)]
        r1,c1 = 0,0
        r2,c2 = len(new)-1,len(new[0])-1
        val = 1
        
        while(c1<=c2 and r1<=r2):
            for (x,y) in helper(r1,r2,c1,c2):
                new[x][y] = val
                val+=1
            r1+=1
            c1+=1
            r2-=1
            c2-=1
        
        return new
