# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def height(root):
            if(not root):
                return(0,None)
            
            left = height(root.left)
            right = height(root.right)
            if(left[0]>right[0]):
                return(left[0]+1,left[1])
            elif(right[0]>left[0]):
                return(right[0]+1,right[1])
            else:
                return(left[0]+1,root)
            
        return(height(root)[1])
            
