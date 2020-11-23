class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        Approach:
        DFS
        First, we search for '1' in the grid. 
        Second, we call a method to change this '1' to '0. Also, we check for the neigboring '1's(only vertical and
        horizontal neighbors) and set their value to '0'(connected components form an island).
        Third, there is an if condition to return 0, incase we go outside the grid or the grid value is '0'.
        For example, if grid[0][0]=='1' and we check the upper horizontal neighbor which doesn't exist, then it means that
        it's value is '0'(water)
        """
        if(grid==None):
            return(0)
        count = 0
        def dfs(i,j):
            if(i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]=='0'):
                return(0)
            else:
                grid[i][j] = '0'
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
                return(1)

        count = [dfs(i,j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j]=='1']
        return(sum(count))
# BFS Approach
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return(0)
        def valid(i,j):
            if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0'):
                return(False)
            return(True)
        
        def bfs(i,j):
            queue = collections.deque()
            queue.append((i,j))
            directions = [(0,-1),(-1,0),(0,1),(1,0)]
            grid[i][j] = '0'
            while(queue):
                x,y = queue.popleft()
                for d in directions:
                    nx,ny = x + d[0],y + d[1]
                    if(valid(nx,ny)):
                        queue.append((nx,ny))
                        grid[nx][ny]='0'
            return(1)
                                
        ans=[bfs(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]=='1']
        return(sum(ans))
            

        
    
            
            
                
