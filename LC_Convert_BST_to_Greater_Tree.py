# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        
        Approach:
        
        Reverse in-order traversal. Go down and then keep adding from there.
        """
        self.sums = 0
        def helper(root):
            if root:
                helper(root.right)
                self.sums+=root.val
                root.val = self.sums
                helper(root.left)
                
        helper(root)
        return(root)
