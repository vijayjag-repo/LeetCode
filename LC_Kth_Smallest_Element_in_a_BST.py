# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def helper(root):
            if not root:
                return([])
        
            return(helper(root.left)+[root.val]+helper(root.right))
        
        return(helper(root)[k-1])
        
        
            
        
