# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def helper(root):
            if not root:
                return(0)
            else:
                left = helper(root.left)
                right = helper(root.right)
                self.ans = max(self.ans,left+right)
                return(max(left,right)+1)
        
        helper(root)
        return(self.ans)
