## Solution 1: DFS approach
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        len_row = len(image)
        len_col = len(image[0])
        target_cell = image[sr][sc]

        def dfs(i,j):
            if (i<0 or i>=len_row or j<0 or j>=len_col or image[i][j] == color or image[i][j] != target_cell):
                return

            image[i][j] = color

            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        dfs(sr, sc)
        return image

## Solution 2: BFS approach
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        len_row = len(image)
        len_col = len(image[0])
        target_cell = image[sr][sc]

        if target_cell != color:
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = color
                for x, y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if (0<=x<len_row and 0<=y<len_col and image[x][y] == target_cell):
                        q.append((x, y))
        return image
