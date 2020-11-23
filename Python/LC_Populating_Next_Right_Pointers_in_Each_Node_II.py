"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return 
        queue, nextLevel = [root], []   
        while queue:
            curr = queue.pop(0)
            if curr.left:
                nextLevel.append(curr.left)
            if curr.right:
                nextLevel.append(curr.right)
            if queue:
                curr.next = queue[0]
            if not queue and nextLevel:
                queue, nextLevel = nextLevel, queue
        
        return(root)
