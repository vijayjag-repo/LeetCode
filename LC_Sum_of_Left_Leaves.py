# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 0
        def helper(root):
            if not root:
                return(0)
            elif(root.left and not root.left.left and not root.left.right):
                    self.ans+=root.left.val
                    
            helper(root.left)
            helper(root.right)
                    
        helper(root)
        return(self.ans)
                    
                
