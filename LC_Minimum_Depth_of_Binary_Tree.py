# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
      
        if not root:
            return(0)
        if(root.left==None or root.right==None):
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return(left+right+1)
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return(min(left,right)+1)
            
        
        
