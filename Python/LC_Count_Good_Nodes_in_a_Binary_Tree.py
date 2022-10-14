# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [(root, float('-inf'))]
        ans = 0

        while stack:
            node, max_val = stack.pop()
            if max_val <= node.val:
                ans += 1
            if node.left:
                stack.append((node.left, max(max_val, node.val)))
            if node.right:
                stack.append((node.right, max(max_val, node.val)))
        return ans
