class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]

        DFS approach:

        Much of the solution is the classic DFS template and cell validation.
        Key idea is to start performing DFS on all the shore cells of the island rather than every cell because we know that water has to flow out from this cell.

        For Pacific ocean, shore cells would be row = 0, all columns and all rows, col = 0
        For atlantic ocean, shore cells would be row = len(height), all colums and all rows, col = len(height[0])

        Base condition is very simple, if the neighboring cell has a height >= current cell, call dfs.
        Also keep track of every cell visited in a set. And since we've to find out the cells from which water would flow into both oceans,
        we will maintain two sets with cell indexes. Finally, we will return the intersection of both these sets.

        Time complexity: O(m * n)
        Space complexity: O(m * n) [Due to recursion call stack]
        """
        p = set()
        a = set()

        def valid_cell(i, j):
            if (0 <= i < len(heights) and 0 <= j < len(heights[0])):
                return True
            return False

        def dfs(i, j, seen):
            if (i, j) in seen:
                return
            seen.add((i, j))

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (valid_cell(x, y)):
                    if (heights[x][y] >= heights[i][j]):
                        dfs(x, y, seen)

        for row in range(len(heights)):
            dfs(row, 0, p)
            dfs(row, len(heights[0]) - 1, a)

        for col in range(len(heights[0])):
            dfs(0, col, p)
            dfs(len(heights) - 1, col, a)

        return list(a & p)
