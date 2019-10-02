# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        
        Approach:
        
        Just use the conditions to traverse left/right depending on the root.val.
        If root.val<L, then you need to go right.
        If root.val>R, then you need to go left.
        Otherwise, the current root is good and you continue to go left and right.
        
        """
        def trim(root,L,R):
            if not root:
                return None
            elif(root.val<L):
                return(trim(root.right,L,R))
            elif(root.val>R):
                return(trim(root.left,L,R))
            else:
                root.left = trim(root.left,L,R)
                root.right = trim(root.right,L,R)
                return(root)
        return(trim(root,L,R))
        
