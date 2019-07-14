# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(preorder,inorder):
            if inorder:
                index = inorder.index(preorder.pop(0))
                root = TreeNode(inorder[index])
                root.left = build(preorder,inorder[:index])
                root.right = build(preorder,inorder[index+1:])
                return(root)
        
        return(build(preorder,inorder))
