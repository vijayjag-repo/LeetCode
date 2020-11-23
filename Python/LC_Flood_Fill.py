class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image:
            return(None)
        m = len(image)
        n = len(image[0])
        old_val = image[sr][sc]
        
        if(old_val==newColor):
            return(image)
        
        def dfs(i,j):
            if(i<0 or i>=m or j<0 or j>=n or image[i][j]!=old_val):
                return
            elif(image[i][j]==old_val and 0<=i<m and 0<=j<n):
                image[i][j] = newColor
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
        
        dfs(sr,sc)
        return(image)