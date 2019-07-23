# Recursive, BFS(Queue) and Stack approach
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        Recursive Solution
        """
        if not root:
            return(0)
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return(1+max(left,right)

# Using Queue - BFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        level = [root] if root else []
        
        while(level):
            depth+=1
            current = []
            for node in level:
                if(node.left):
                    current.append(node.left)
                if(node.right):
                    current.append(node.right)
                    
            level = current
        return(depth)
                   
# Using Stack
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        depth = 0
        stack.append((root,1))
        
        while(stack):
            root,current_depth = stack.pop()
            if(not root):
                return(0)
            depth = max(depth,current_depth)
            if(root.left):
                stack.append((root.left,current_depth+1))
            if(root.right):
                stack.append((root.right,current_depth+1))
            
        return(depth)

             
