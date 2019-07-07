"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def __init__(self):
        self.visited = {}
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        visited = dict()
        m = n = head
        while m:
            visited[m] = Node(m.val,None,None)
            m = m.next
        while n:
            visited[n].next = visited.get(n.next)
            visited[n].random = visited.get(n.random)
            n = n.next
        return visited.get(head)
