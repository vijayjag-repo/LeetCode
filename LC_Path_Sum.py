# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        
        Approach:
        
        As and when you go along a path, pass on difference in sum left.
        If we reach a leaf node, we check if the difference is equal to the leaf node val. 
        """
        def helper(root,sum):
            if not root:
                return(False)
            elif(not root.left and not root.right):
                return(sum==root.val)
            else:
                return(self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val))
        
        return(helper(root,sum))
