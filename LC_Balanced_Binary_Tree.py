# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        Approach:
        
        Find depth recursively.
        Store the max_difference between depths of left and right subtrees. 
        If this value is greater than 1, it is not balanced. Else, balanced.
        """
        
        self.max_difference = 0
        def helper(root):
            if not root:
                return(0)
            else:
                left = helper(root.left)
                right = helper(root.right)
                self.max_difference = max(self.max_difference,abs(left-right))
                return(1+max(left,right))
        
        helper(root)
        return(False if self.max_difference>1 else True)
