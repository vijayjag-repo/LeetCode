class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool

        Approach:

        First step is to build a graph based on the input we have.
        After that, start from the source and perform DFS to check for destination
        Same could be done with BFS as well and only thing we need to change is whether we pop from left or right.

        Time complexity: O(m + n)
        Space complexity: O(m + n)
        """
        graph = [[] for i in range(n)]
        q = collections.deque([(source)])
        seen = set()

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(q, destination):
            while q:
                node = q.pop()
                if node == destination:
                    return True
                else:
                    for neighbor in graph[node]:
                        if neighbor not in seen:
                            q.append(neighbor)
                            seen.add(neighbor)
            return False

        return dfs(q, destination)
