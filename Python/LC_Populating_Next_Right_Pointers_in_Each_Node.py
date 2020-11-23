# Recursive Approach:
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
        
        Approach:
        Connect the left child to the right and connect the right to the left of next. Recursively.
        """
        if root and root.left and root.right:
            root.left.next = root.right
            if(root.next):
                root.right.next = root.next.left
            
            self.connect(root.left)
            self.connect(root.right)
        return(root)
