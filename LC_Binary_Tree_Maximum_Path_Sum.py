# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        Approach:
        Keep going down the tree. Keep adding the sums. If the sum at any point is -ve, reset it to 0.
        Finally, return the global maximum value.
        
        """
        self.globalmax = float('-inf')
        def helper(root):
            if not root:
                return(0)
            left = helper(root.left)
            right = helper(root.right)
            self.globalmax = max(left+right+root.val,self.globalmax)
            return(max(max(left,right)+root.val,0))
        helper(root)
        return(self.globalmax)
