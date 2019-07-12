# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return(None)
        self.min_node = 0
        self.min_val = float('inf')
        def helper(root,target):
            if not root:
                return
            else:
                if(abs(root.val-target)<self.min_val):
                    self.min_val = abs(root.val-target)
                    self.min_node = root.val
                
                helper(root.left,target)
                helper(root.right,target)
        
        helper(root,target)
        return(self.min_node)
                    
