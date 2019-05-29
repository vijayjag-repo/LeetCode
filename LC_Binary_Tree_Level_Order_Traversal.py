# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return(levels)
        
        def helper(root,level):
            if(len(levels)==level):
                levels.append([])
            
            levels[level].append(root.val)
            if(root.left):
                helper(root.left,level+1)
            if(root.right):
                helper(root.right,level+1)
                
        helper(root,0)
        return(levels)
