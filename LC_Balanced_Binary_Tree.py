# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Use height method to find the height/depth of the subtrees. Similar to maximum Depth problem.
# Since we are comparing the subtrees of each node, you find out the respective heights of subtrees for each node.
# If both the subtrees obey the rule, return True, else return False

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return(True)
        else:
            l = self.height(root.left)
            r = self.height(root.right)
            if(abs(l-r)>1):
                return(False)
            return(self.isBalanced(root.left) and self.isBalanced(root.right))
        
    def height(self,root):
        if not root:
            return(0)
        else:
            left = self.height(root.left)
            right = self.height(root.right)
            return(max(left,right)+1)
