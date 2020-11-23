# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        Approach:
        
        Pretty simple. Go to each node and if it doesn't have a left, right child, append it to the list.
        Do the same for both the TreeNodes and compare them.
        """
        def helper(root):
            if not root:
                return([])
            else:
                if not root.left and not root.right:
                    return([root.val])
                else:
                    return(helper(root.left)+helper(root.right))
            
        return(helper(root1)==helper(root2))
        
        
