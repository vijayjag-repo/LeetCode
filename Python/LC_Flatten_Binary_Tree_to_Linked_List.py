# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return([])
        
        stack = [root]
        tree = TreeNode(-1)
        
        while(stack):
            node = stack.pop()
            tree.right = node
            tree.left = None
            if(node.right):
                stack.append(node.right)
            if(node.left):
                stack.append(node.left)
            
            tree = node
        
                
