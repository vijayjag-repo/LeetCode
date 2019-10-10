import collections
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        Approach:
        
        Easy hack would be to append to a list for every level that you see from the bottom.
        """
        d = collections.defaultdict(list)
        def helper(root):
            if not root:
                return 0
            else:
                left = helper(root.left)
                right = helper(root.right)
                level = max(left,right)+1
                d[level].append(root.val)
                return level
        
        helper(root)
        return d.values()
