# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(0)
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            if(left>right):
                return(left+1)
            else:
                return(right+1)
