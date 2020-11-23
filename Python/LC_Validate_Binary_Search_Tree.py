# Iterative method with less space
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
        Approach:
        
        First you store only the left nodes. the leftmost node will have the least value in the BST.
        """
        stack = []
        inorder = float('-inf')
        
        while(stack or root):
            while(root):
                stack.append(root)
                root = root.left
            root = stack.pop()
            if(root.val<=inorder):
                return(False)
            inorder = root.val
            root = root.right
        return(True)
    
# Recursive method
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
        def helper(node,lower=float('-inf'),upper=float('inf')):
            if not node:
                return(True)
            
            val = node.val
            if(val<=lower or val>=upper):
                return(False)
            
            if not helper(node.right,val,upper):
                return(False)
            if not helper(node.left,lower,val):
                return(False)
            return(True)
        return(helper(root))
    
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
        
        Approach:
        
        This approach makes use of inorder traversal and goes through the tree entirely.
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
