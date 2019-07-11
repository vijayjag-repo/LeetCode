# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if(root):
            if(val>root.val):
                return(self.searchBST(root.right,val))
            elif(val<root.val):
                return(self.searchBST(root.left,val))
            else:
                return(root)
        
        
            
            
