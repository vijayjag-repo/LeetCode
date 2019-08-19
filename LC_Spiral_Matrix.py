class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        Approach:
        
        Use generators.
        First workout the first pattern or layer.
        Repeat this by going to next layer. 
        Typically, you do 4 iterations(First row, last column, last row, first column). Then you keep going in.
        """
        ans = []
        if not matrix:
            return(ans)
        
        def get(r1,c1,r2,c2):
            for c in range(c1,c2+1):
                yield r1,c
            for r in range(r1+1,r2+1):
                yield r,c2
            if(r2>r1 and c2>c1):
                for c in range(c2-1,c1-1,-1):
                    yield r2,c
                for r in range(r2-1,r1,-1):
                    yield r,c1
        
        r1 = c1 = 0
        r2 = len(matrix)-1
        c2 = len(matrix[0])-1
        
        while(c1<=c2 and r1<=r2):
            for (x,y) in get(r1,c1,r2,c2):
                ans.append(matrix[x][y])
                
            r1+=1
            c1+=1
            r2-=1
            c2-=1
        return(ans)
