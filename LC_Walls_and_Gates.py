class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.

        """
        def valid(x,y,count):
            if(x<0 or x>=len(rooms) or y<0 or y>=len(rooms[0]) or rooms[x][y]<count):
                return False
            return True
        
        def dfs(i,j,count):
            if(valid(i,j,count)):
                rooms[i][j] = count
                dfs(i-1,j,count+1)
                dfs(i+1,j,count+1)
                dfs(i,j-1,count+1)
                dfs(i,j+1,count+1)
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if(rooms[i][j]==0):
                    dfs(i,j,0)
                    
        
        
       
        
            
