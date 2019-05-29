# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        new = []
        def helper(root):
            if not root:
                return([])
            return(helper(root.left)+[root.val]+helper(root.right))
        
        new = helper(root)
        for i in range(len(new)-1):
            if(new[i]>=new[i+1]):
                return(False)
        return(True)
