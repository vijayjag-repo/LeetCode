# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build(postorder,inorder):
            if inorder:
                index = inorder.index(postorder.pop())
                root = TreeNode(inorder[index])
                root.right = build(postorder,inorder[index+1:])
                root.left = build(postorder,inorder[:index])
                return(root)
        
        return(build(postorder,inorder))
