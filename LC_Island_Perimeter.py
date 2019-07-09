#Two Approaches. 
# First One. Little faster compared to the second approach.
# Key takeaway for this problem is that you shouldn't update the cell that you already saw.
# (i.e) In similar DFS questions, we update the seen cell to '0' but here if we do that, we can't find the perimeter.
# Because, you need the number of neighbors to calculate whether there is an edge on each side or not.

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        Approach:
        Straightforward. Check the neighbors. If it isn't 1, add it to the perimeter. (Diagram helped for visualization)
        """
        if not grid:
            return(0)
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for x in range(m):
            for y in range(n):
                if(grid[x][y]):
                    if(x-1<0 or grid[x-1][y]!=1):
                        count+=1
                    if(x+1>=m or grid[x+1][y]!=1):
                        count+=1
                    if(y-1<0 or grid[x][y-1]!=1):
                        count+=1
                    if(y+1>=n or grid[x][y+1]!=1):
                        count+=1
                              
        return(count)
        
#Approach 2
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        Approach:
        This is the classic dfs approach.
        """
        if not grid:
            return(0)
        
        m = len(grid)
        n = len(grid[0])
        
        def adj(i,j):
            sums = 0
            for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if(x<0 or y<0 or x==m or y==n or grid[x][y]==0):
                    sums+=1
            return(sums)
                
        count = 0
        for x in range(m):
            for y in range(n):
                if(grid[x][y]):
                    count+=adj(x,y)
        return(count)
