# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        def helper(root, parent):
            if not root:
                return True
            left = helper(root.left, root.val)
            right = helper(root.right, root.val)
            if left and right:
                self.count += 1
            return left and right and root.val == parent

        helper(root, None)
        return self.count
