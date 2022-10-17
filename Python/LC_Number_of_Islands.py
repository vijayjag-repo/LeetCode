# DFS approach
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        Intuition: If we find land (1 == land and 0 == water), then we search all its neighbors to find land as well.
        If there's no land and only water, we've found our exit condition to add one island to our count.

        1. Search for '1' in the grid.
        2. From the current position, call all 4 neighbors (vertical and horizontal) to find if they are '1' or not(ie: land or not)
        3. Since we're employing DFS here, this traversal will continue as long as we continue to find '1'.
        4. One key idea to remember - we should change the value of the land that we've already visited to '0'.
            We need to do this because, we could get stuck in an infinite loop.
        5. Additionally, we also need to ensure that a given cell is land (index within the grid and not equal to water)
        6. Once the DFS call ends, that means we've found an island. Increment the count
        7. Now, we have successfully turned an island of '1's into '0's. Repeat step 1 for the remaining '1's and finally return count.

        Time complexity: O(m * n)
        Space complexity: O(m * n)
        """
        no_of_islands = 0

        def valid_cell(row, col):
            if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0'):
                return False
            return True

        def dfs(row, col):
            if (not valid_cell(row, col)):
                return 0
            else:
                grid[row][col] = '0'
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
                return 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == '1'):
                    no_of_islands += dfs(i, j)

        return no_of_islands

# BFS Approach
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        Same as DFS approach but the only variation is that,
        while looking at a given '1', we only traverse the immediate 4 neighbors of this cell and not their neighbors and so on.
        And to do that, we'll be using a deque instead of a stack to pop elements from the left.

        Time complexity: O(m * n)
        Space complexity: O(min(m,n))
        """
        no_of_islands = 0

        def valid_cell(row, col):
            if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0'):
                return False
            return True

        def bfs(row, col):
            q = collections.deque([(row, col)])
            grid[row][col] = '0'
            while q:
                row, col = q.popleft()
                for (x, y) in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    if (valid_cell(x, y)):
                        q.append((x, y))
                        grid[x][y] = '0'
            return 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == '1'):
                    no_of_islands += bfs(i, j)

        return no_of_islands
