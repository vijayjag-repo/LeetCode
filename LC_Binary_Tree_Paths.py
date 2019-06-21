# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        def traverse(root,path):
            if root:
                path+=str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path+='->'
                    traverse(root.left,path)
                    traverse(root.right,path)
        
        traverse(root,"")
        return(paths)
        
